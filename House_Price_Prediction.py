import pandas as pd
from tkinter import Tk, Label, StringVar, Button, messagebox, Frame
from tkinter.ttk import Combobox
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer
from xgboost import XGBRegressor

# Load and preprocess the dataset
file_path = 'C:\\Users\\PRASOON\\Desktop\\Notes\\Minor Project\\FILLVALUE_Housing_data.csv'
data = pd.read_csv(file_path)

# Filter and preprocess data
data = data[data['List Year'] <= 2020]  # Filter relevant years

# Define encoders
le_town = LabelEncoder()
data['Town'] = le_town.fit_transform(data['Town'])

# Collect all unique types from both columns
property_type_options = sorted(
    set(data['Property Type'].unique()).union(data['Residential Type'].unique())
)

# Apply one-hot encoding to the Property Type and Residential Type with `handle_unknown='ignore'`
onehotencoder = ColumnTransformer(
    transformers=[
        ('property_type', OneHotEncoder(handle_unknown='ignore'), ['Property Type']),
        ('residential_type', OneHotEncoder(handle_unknown='ignore'), ['Residential Type'])
    ],
    remainder='passthrough'
)

# Prepare data for training
X = data[['List Year', 'Town', 'Property Type', 'Residential Type', 'Assessed Value']]
y = data['Sale Amount']
X_encoded = onehotencoder.fit_transform(X)

# Train-test split
X_train = X_encoded[X['List Year'] <= 2016]
y_train = y[X['List Year'] <= 2016]

# Train the model
model = XGBRegressor(n_estimators=100, learning_rate=0.1, max_depth=5, random_state=42)
model.fit(X_train, y_train)

# Unique options for dropdowns
town_options = le_town.classes_.tolist()
year_options = ["2023", "2024", "2025"]

# Build the tkinter UI
root = Tk()
root.title("House Price Prediction")
root.geometry("600x400")  # Initial size
root.configure(bg="#f5f5f5")

# Centering Frame for all content
main_frame = Frame(root, bg="#f5f5f5")
main_frame.pack(fill="both", expand=True)

# Inner Frame for centered content
content_frame = Frame(main_frame, bg="#f5f5f5")
content_frame.place(relx=0.5, rely=0.5, anchor="center")

# Styles for labels and option menus
label_font = ("Arial", 12, "bold")
dropdown_font = ("Arial", 10)
button_font = ("Arial", 12, "bold")
heading_font = ("Arial", 18, "bold")

# Heading
heading_label = Label(content_frame, text="House Price Predictor", font=heading_font, fg="#333", bg="#f5f5f5")
heading_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))

Label(content_frame, text="Select Location (Town):", font=label_font, bg="#f5f5f5").grid(row=1, column=0, pady=5, sticky="w")
location_var = StringVar(root)
location_var.set("Town")  # Default placeholder text
location_combobox = Combobox(content_frame, textvariable=location_var, values=town_options, font=dropdown_font, width=20)
location_combobox.grid(row=1, column=1, pady=5)

# Year dropdown
Label(content_frame, text="Select Year (Current / 2nd Year / 3rd Year):", font=label_font, bg="#f5f5f5").grid(row=2, column=0, pady=5, sticky="w")
year_var = StringVar(root)
year_menu = Combobox(content_frame, textvariable=year_var, values=year_options, font=dropdown_font, width=20)
year_menu.grid(row=2, column=1, pady=5)
# year_menu.set(year_options[0])  # Default value
year_menu.set("Year")  # Default value

# Type of House dropdown with extended options
Label(content_frame, text="Select Type of House:", font=label_font, bg="#f5f5f5").grid(row=3, column=0, pady=5, sticky="w")
house_type_var = StringVar(root)
house_type_menu = Combobox(content_frame, textvariable=house_type_var, values=property_type_options, font=dropdown_font, width=20)
house_type_menu.grid(row=3, column=1, pady=5)
house_type_menu.set("House Type")  # Default value
# house_type_menu.set(property_type_options[0])  # Default value

def predict_price():
    try:
        # Get user inputs
        location = location_var.get()
        year = year_var.get()
        house_type = house_type_var.get()

        # Check if any input is missing
        if location == "Select a location" or not year or house_type == "Select a type":
            messagebox.showwarning("Input Error", "Please enter correct inputs.")
            return

        # Check if the town is known to the LabelEncoder
        if location not in le_town.classes_:
            messagebox.showwarning("Input Error", "Please enter correct inputs.")
            return

        # Process inputs if all are filled
        location_encoded = le_town.transform([location])[0]
        year = int(year)  # Convert year to integer

        # Prepare data for one-hot encoding and prediction
        input_data = pd.DataFrame({
            'List Year': [year],
            'Town': [location_encoded],
            'Property Type': [house_type],
            'Residential Type': [house_type],
            'Assessed Value': [0]  # Placeholder
        })

        # One-hot encode the input
        input_encoded = onehotencoder.transform(input_data)

        # Predict
        predicted_price = model.predict(input_encoded)[0]
        messagebox.showinfo("Prediction", f"Predicted House Price: ${predicted_price:,.2f}")

    except Exception:
        # Show a general error message for any exception
        messagebox.showerror("Error", "Please enter correct inputs.")




# Button to trigger prediction
predict_button = Button(content_frame, text="Predict Price", font=button_font, bg="#4CAF50", fg="white", command=predict_price)
predict_button.grid(row=4, column=1, pady=20, sticky="e")

root.mainloop()