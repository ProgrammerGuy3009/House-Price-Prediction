# 🏠 House Price Prediction Model (Tkinter + XGBoost)

A desktop-based machine learning application to predict house prices using **XGBoost** and an interactive **Tkinter GUI**. The model is trained on real-world housing data and allows users to select a town, year, and property type to get a predicted sale amount.

> 🔗 Featured in my portfolio: ((https://github.com/ProgrammerGuy3009/ProgrammerGuy3009/blob/main/README.md))

---

## 🚀 Features

- 📊 Trained using **XGBoost Regressor** with >85% R² accuracy
- 🎛️ Simple and intuitive **Tkinter interface**
- 🏡 Dynamic dropdowns for town, year, and property type
- ⚡ Real-time predictions with instant UI response
- ⚠️ Built-in input validation and error messages

---

## 💻 Tech Stack

| Category         | Technology Used                     |
|------------------|-------------------------------------|
| Language         | Python                              |
| Libraries        | pandas, scikit-learn, XGBoost       |
| GUI Framework    | Tkinter + ttk Combobox              |
| ML Techniques    | Label Encoding, One-Hot Encoding    |
| Model            | XGBRegressor                        |

---

## 📷 Screenshots

### 🖥️ Main Interface  
![image](https://github.com/user-attachments/assets/9941877a-0dc0-47f7-981d-3dbccd1b1648)


### 🏡 Prediction Example  
![image](https://github.com/user-attachments/assets/88416df1-259b-4145-8a4e-61aecc6f7ba3)


---
## 📥 Dataset Source

The dataset used in this project is publicly available on Kaggle:  
👉 [Real Estate Sales 2001–2022 – Kaggle](https://www.kaggle.com/datasets/omniamahmoudsaeed/real-estate-sales-2001-2022)

---
## 🧠 How It Works

1. **Preprocess the Dataset**
   - Filters data up to the year 2020
   - Encodes categorical features like town, property type, residential type

2. **Model Training**
   - Uses `XGBRegressor` trained on housing sale amounts from years up to 2016
   - One-hot encoded features are passed for better handling of category levels

3. **User Interface**
   - Built with Tkinter and ttk
   - User selects:
     - Location (Town)
     - Target Year (2023–2025)
     - Type of Property
   - Predicts and displays expected house price

---

## 🛠️ How to Run

### ✅ Requirements

- Python 3.8+
- Libraries: `pandas`, `scikit-learn`, `xgboost`, `tkinter`

```bash
pip install pandas scikit-learn xgboost
