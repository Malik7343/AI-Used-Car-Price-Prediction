import streamlit as st
import joblib
import pandas as pd
import requests
from pathlib import Path

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="AI Used Car Price Prediction",
    page_icon="🚗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -----------------------------
# LOAD MODEL (downloads from Hugging Face if not present locally)
# -----------------------------
MODEL_PATH = Path("backend/models/used_car_price_model.joblib")

# TODO: replace with YOUR Hugging Face username/repo name
HF_MODEL_URL = "https://huggingface.co/Malik7343/used-car-price-model1/resolve/main/used_car_price_model.joblib"

@st.cache_resource
def load_model():
    if not MODEL_PATH.exists():
        MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
        with st.spinner("Downloading model (first run only)..."):
            response = requests.get(HF_MODEL_URL, stream=True)
            response.raise_for_status()
            with open(MODEL_PATH, "wb") as f:
                for chunk in response.iter_content(chunk_size=8192):
                    f.write(chunk)
    return joblib.load(MODEL_PATH)

model = load_model()

# -----------------------------
# CUSTOM CSS
# -----------------------------
st.markdown("""
<style>

/* App background */
.stApp{
background:linear-gradient(135deg,#0F172A,#111827,#1E293B);
}

/* Hide default streamlit padding at top */
.block-container{
padding-top:2rem;
padding-bottom:3rem;
max-width:1200px;
}

/* Title */
.main-title{
font-size:46px;
font-weight:800;
color:white;
text-align:center;
letter-spacing:-1px;
margin-bottom:4px;
}

.subtitle{
font-size:17px;
color:#94a3b8;
text-align:center;
margin-bottom:30px;
font-weight:400;
}

/* Glass card wrapper used around the form */
.glass-card{
background:rgba(255,255,255,0.05);
border:1px solid rgba(255,255,255,0.08);
padding:32px 32px 12px 32px;
border-radius:20px;
backdrop-filter:blur(12px);
margin-bottom:24px;
box-shadow:0 8px 32px rgba(0,0,0,0.25);
}

.section-heading{
color:#e2e8f0;
font-size:22px;
font-weight:700;
margin-bottom:18px;
border-left:4px solid #22c55e;
padding-left:12px;
}

/* Metric cards at top */
div[data-testid="stMetric"]{
background:rgba(255,255,255,0.06);
border:1px solid rgba(255,255,255,0.08);
padding:18px 10px;
border-radius:16px;
text-align:center;
}

div[data-testid="stMetricLabel"]{
color:#94a3b8 !important;
justify-content:center;
}

div[data-testid="stMetricValue"]{
color:#22c55e !important;
justify-content:center;
}

/* Input labels */
label, .stSelectbox label, .stNumberInput label, .stTextInput label{
color:#cbd5e1 !important;
font-weight:600 !important;
font-size:13px !important;
text-transform:uppercase;
letter-spacing:0.5px;
}

/* Text inputs, number inputs, selectboxes */
.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] > div{
background-color:#1e293b !important;
color:white !important;
border:1px solid rgba(255,255,255,0.12) !important;
border-radius:10px !important;
}

.stTextInput input:focus,
.stNumberInput input:focus{
border:1px solid #22c55e !important;
box-shadow:0 0 0 1px #22c55e !important;
}

/* Dropdown menu items */
ul[role="listbox"]{
background-color:#1e293b !important;
}

li[role="option"]{
color:white !important;
}

/* Plus / minus buttons on number input */
.stNumberInput button{
background-color:#334155 !important;
border:none !important;
color:white !important;
}

/* Predict button */
.stButton button{
background:linear-gradient(135deg,#22c55e,#16a34a);
color:white;
font-weight:700;
font-size:17px;
border:none;
border-radius:12px;
padding:14px 0;
transition:all 0.2s ease-in-out;
box-shadow:0 4px 20px rgba(34,197,94,0.35);
}

.stButton button:hover{
transform:translateY(-2px);
box-shadow:0 6px 24px rgba(34,197,94,0.5);
}

/* Result cards */
.metric-card{
background:linear-gradient(135deg,#111827,#1e293b);
padding:28px;
border-radius:18px;
text-align:center;
color:white;
border:1px solid rgba(255,255,255,0.08);
height:100%;
}

hr{
border-color:rgba(255,255,255,0.08) !important;
}

/* Sidebar */
section[data-testid="stSidebar"]{
background:#0b1120;
border-right:1px solid rgba(255,255,255,0.06);
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:

    st.title("🚗 AI Predictor")

    st.markdown("---")

    st.success("Model Loaded Successfully")

    st.markdown("### About")

    st.write("""
This application predicts the market value
of used cars using Machine Learning.
""")

    st.markdown("---")

    st.info("Random Forest Regressor")

# -----------------------------
# HEADER
# -----------------------------
st.markdown(
"""
<div class="main-title">🚗 AI Used Car Price Prediction</div>
<div class="subtitle">Premium Machine Learning Dashboard</div>
""",
unsafe_allow_html=True
)

# -----------------------------
# STATS
# -----------------------------
c1,c2,c3,c4=st.columns(4)

c1.metric("Accuracy","89.4%")
c2.metric("Model","Random Forest")
c3.metric("Dataset","15K+")
c4.metric("Status","Online")

st.write("")

# -----------------------------
# FORM (wrapped in a glass card)
# -----------------------------
st.markdown('<div class="glass-card">', unsafe_allow_html=True)

st.markdown('<div class="section-heading">Car Information</div>', unsafe_allow_html=True)

col1,col2=st.columns(2, gap="large")

with col1:

    car_name=st.text_input("Car Name", placeholder="e.g. Alto")

    brand=st.text_input("Brand", placeholder="e.g. Suzuki")

    model_name=st.text_input("Model", placeholder="e.g. 2019")

    vehicle_age=st.number_input(
        "Vehicle Age",
        0,
        30,
        5
    )

    km_driven=st.number_input(
        "KM Driven",
        0,
        500000,
        50000
    )

    seller_type=st.selectbox(
        "Seller Type",
        [
            "Individual",
            "Dealer",
            "Trustmark Dealer"
        ]
    )

with col2:

    fuel_type=st.selectbox(
        "Fuel Type",
        [
            "Petrol",
            "Diesel",
            "CNG",
            "LPG",
            "Electric"
        ]
    )

    transmission_type=st.selectbox(
        "Transmission",
        [
            "Manual",
            "Automatic"
        ]
    )

    mileage=st.number_input(
        "Mileage",
        0.0,
        50.0,
        18.0
    )

    engine=st.number_input(
        "Engine (CC)",
        500,
        5000,
        1200
    )

    max_power=st.number_input(
        "Max Power",
        20.0,
        500.0,
        90.0
    )

    seats=st.number_input(
        "Seats",
        2,
        10,
        5
    )

st.write("")

predict=st.button(
    "🚀 Predict Price",
    use_container_width=True
)

st.markdown('</div>', unsafe_allow_html=True)  # close glass-card

# -----------------------------
# PREDICTION LOGIC
# -----------------------------
if predict:

    if not car_name or not brand or not model_name:
        st.warning("⚠️ Please fill in Car Name, Brand, and Model before predicting.")
    else:
        try:
            input_df = pd.DataFrame([{
                "car_name": car_name,
                "brand": brand,
                "model": model_name,
                "vehicle_age": vehicle_age,
                "km_driven": km_driven,
                "seller_type": seller_type,
                "fuel_type": fuel_type,
                "transmission_type": transmission_type,
                "mileage": mileage,
                "engine": engine,
                "max_power": max_power,
                "seats": seats
            }])

            with st.spinner("Predicting price..."):
                prediction = model.predict(input_df)[0]

            st.write("")
            st.markdown('<div class="glass-card">', unsafe_allow_html=True)
            st.markdown('<div class="section-heading">💰 Predicted Price</div>', unsafe_allow_html=True)

            price_col1, price_col2 = st.columns([2, 1])

            with price_col1:
                st.markdown(
                    f"""
                    <div class="metric-card">
                        <h1 style="color:#22c55e;margin:0;font-size:42px;">₹ {prediction:,.0f}</h1>
                        <p style="color:#9ca3af;margin-top:8px;">Estimated Market Value</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with price_col2:
                st.markdown(
                    f"""
                    <div class="metric-card">
                        <h3 style="margin:0;">{brand} {model_name}</h3>
                        <p style="color:#9ca3af;margin-top:8px;">{vehicle_age} yrs • {km_driven:,} km • {fuel_type}</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            st.write("")
            st.success("✅ Prediction generated successfully!")
            st.markdown('</div>', unsafe_allow_html=True)

        except ValueError as e:
            st.error(
                "❌ Prediction failed — the model likely expects encoded/numeric "
                "features instead of raw text categories."
            )
            st.code(str(e))
            st.info(
                "Fix: either (1) save your model as a full Pipeline "
                "(ColumnTransformer + regressor) so it accepts raw input like this, "
                "or (2) load a saved encoder/scaler here and transform `input_df` "
                "before calling `model.predict()`."
            )

        except Exception as e:
            st.error("❌ Something went wrong during prediction.")
            st.code(str(e))