# 🚗 AI Used Car Price Prediction

A Machine Learning powered web application that predicts the estimated market value of a used car based on its specifications — brand, model, age, mileage, fuel type, engine, and more.

**🔗 Live App:** [ai-used-car-price-prediction.streamlit.app](https://ai-used-car-price-prediction-gca3ytqwhswqym2vfgvuah.streamlit.app)

![Status](https://img.shields.io/badge/status-online-brightgreen)
![Python](https://img.shields.io/badge/python-3.10%2B-blue)
![Streamlit](https://img.shields.io/badge/built%20with-Streamlit-ff4b4b)

---

## 📌 Overview

This project uses a **Random Forest Regressor** trained on 15,000+ used car listings to estimate a fair market price for a vehicle. Users enter details like brand, fuel type, transmission, mileage, and engine capacity through an interactive dashboard, and the model returns an instant price prediction.

---

## ✨ Features

- 🎯 Instant price prediction based on 12+ car attributes
- 🎨 Clean, modern, dashboard-style UI
- ☁️ Model hosted on Hugging Face Hub (downloaded at runtime)
- 📊 Trained on real-world used car listing data
- 🔒 Input validation to prevent incomplete predictions

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend / UI | Streamlit |
| ML Model | scikit-learn (Random Forest Regressor) |
| Data Handling | pandas |
| Model Storage | Hugging Face Hub |
| Deployment | Streamlit Community Cloud |

---

## 🚀 Getting Started (Run Locally)

```bash
# Clone the repository
git clone https://github.com/Malik7343/AI-Used-Car-Price-Prediction.git
cd AI-Used-Car-Price-Prediction

# Create a virtual environment
python -m venv .venv
.venv\Scripts\activate      # Windows
# source .venv/bin/activate  # macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`.

---

## 📂 Project Structure

```
AI-Used-Car-Price-Prediction/
├── app.py                 # Main Streamlit application
├── requirements.txt        # Python dependencies
├── backend/
│   └── models/             # (model downloaded here at runtime)
├── utils/                  # Helper utilities
└── README.md
```

---

## 🧠 Model Inputs

| Feature | Description |
|---|---|
| Car Name | Name/variant of the car |
| Brand | Manufacturer (e.g. Maruti, Hyundai) |
| Model | Model year |
| Vehicle Age | Age of the car in years |
| KM Driven | Total kilometers driven |
| Seller Type | Individual / Dealer / Trustmark Dealer |
| Fuel Type | Petrol / Diesel / CNG / LPG / Electric |
| Transmission | Manual / Automatic |
| Mileage | Fuel efficiency (km/l) |
| Engine | Engine displacement (CC) |
| Max Power | Maximum power output (bhp) |
| Seats | Number of seats |

---

## 📈 Model Performance

- **Accuracy:** ~89.4%
- **Algorithm:** Random Forest Regressor
- **Training Data:** 15,000+ used car listings

---

## 🙋 Author

**Malik Taj Khan**
[GitHub](https://github.com/Malik7343)

---

## 📄 License

This project is open source and available for educational purposes.