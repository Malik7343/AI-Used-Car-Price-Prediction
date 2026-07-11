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
# CUSTOM CSS — MATERIAL / PROFESSIONAL THEME
# -----------------------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

html, body, [class*="css"]  {
    font-family: 'Inter', sans-serif;
}

/* ---------- App background ---------- */
.stApp{
    background: radial-gradient(circle at 20% 0%, #16213e 0%, #0d1321 45%, #090c14 100%);
}

.block-container{
    padding-top: 1.6rem;
    padding-bottom: 3rem;
    max-width: 1180px;
}

/* ---------- Top hero ---------- */
.hero-wrap{
    text-align:center;
    padding: 18px 0 6px 0;
}

.hero-badge{
    display:inline-flex;
    align-items:center;
    gap:6px;
    background:rgba(99,102,241,0.12);
    border:1px solid rgba(99,102,241,0.35);
    color:#a5b4fc;
    font-size:12.5px;
    font-weight:600;
    letter-spacing:0.4px;
    padding:6px 14px;
    border-radius:999px;
    margin-bottom:18px;
}

.main-title{
    font-size:44px;
    font-weight:800;
    color:#f8fafc;
    letter-spacing:-1.2px;
    margin-bottom:6px;
    line-height:1.15;
}

.main-title span{
    background: linear-gradient(90deg,#6366f1,#22c55e);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}

.subtitle{
    font-size:16px;
    color:#94a3b8;
    font-weight:400;
    margin-bottom:8px;
}

/* ---------- Stat / metric cards ---------- */
div[data-testid="stMetric"]{
    background: linear-gradient(145deg, rgba(255,255,255,0.045), rgba(255,255,255,0.015));
    border:1px solid rgba(255,255,255,0.08);
    padding:20px 14px;
    border-radius:18px;
    text-align:center;
    box-shadow: 0 6px 20px rgba(0,0,0,0.25);
    transition: transform 0.18s ease, box-shadow 0.18s ease;
}
div[data-testid="stMetric"]:hover{
    transform: translateY(-3px);
    box-shadow: 0 10px 28px rgba(0,0,0,0.35);
    border-color: rgba(99,102,241,0.4);
}
div[data-testid="stMetricLabel"]{
    color:#94a3b8 !important;
    justify-content:center;
    font-size:11.5px !important;
    letter-spacing:1px;
    text-transform:uppercase;
    font-weight:700 !important;
}
div[data-testid="stMetricValue"]{
    color:#f1f5f9 !important;
    justify-content:center;
    font-size:26px !important;
    font-weight:800 !important;
}

/* ---------- Section card ---------- */
.section-card{
    background: linear-gradient(160deg, rgba(255,255,255,0.055), rgba(255,255,255,0.02));
    border:1px solid rgba(255,255,255,0.09);
    padding:30px 32px 16px 32px;
    border-radius:22px;
    backdrop-filter: blur(14px);
    margin-bottom:26px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.3);
}

.section-title{
    display:flex;
    align-items:center;
    gap:10px;
    color:#f1f5f9;
    font-size:20px;
    font-weight:700;
    margin-bottom:4px;
}

.section-sub{
    color:#7c869a;
    font-size:13.5px;
    margin-bottom:22px;
}

.field-group-label{
    color:#818cf8;
    font-size:12px;
    font-weight:700;
    letter-spacing:1.2px;
    text-transform:uppercase;
    margin: 6px 0 2px 0;
}

/* ---------- Labels ---------- */
label, .stSelectbox label, .stNumberInput label, .stTextInput label{
    color:#cbd5e1 !important;
    font-weight:600 !important;
    font-size:12.5px !important;
    text-transform:uppercase;
    letter-spacing:0.6px;
}

/* ---------- Inputs ---------- */
.stTextInput input,
.stNumberInput input,
.stSelectbox div[data-baseweb="select"] > div{
    background-color:#141b2e !important;
    color:#f1f5f9 !important;
    border:1px solid rgba(255,255,255,0.1) !important;
    border-radius:12px !important;
    font-size:14.5px !important;
}

.stTextInput input::placeholder{
    color:#556077 !important;
}

.stTextInput input:focus,
.stNumberInput input:focus{
    border:1px solid #6366f1 !important;
    box-shadow: 0 0 0 3px rgba(99,102,241,0.18) !important;
}

ul[role="listbox"]{ background-color:#141b2e !important; }
li[role="option"]{ color:#f1f5f9 !important; }

.stNumberInput button{
    background-color:#1e293b !important;
    border:none !important;
    color:#cbd5e1 !important;
}

/* ---------- Predict button ---------- */
.stButton button{
    background: linear-gradient(135deg,#6366f1,#4338ca);
    color:white;
    font-weight:700;
    font-size:16px;
    border:none;
    border-radius:14px;
    padding:15px 0;
    letter-spacing:0.3px;
    transition: all 0.2s ease-in-out;
    box-shadow: 0 8px 24px rgba(99,102,241,0.35);
}
.stButton button:hover{
    transform: translateY(-2px);
    box-shadow: 0 12px 30px rgba(99,102,241,0.5);
}
.stButton button:active{
    transform: translateY(0px);
}

/* ---------- Result cards ---------- */
.result-hero{
    background: linear-gradient(135deg, rgba(34,197,94,0.14), rgba(34,197,94,0.02));
    border:1px solid rgba(34,197,94,0.35);
    padding:34px;
    border-radius:20px;
    text-align:center;
}
.result-price{
    font-size:46px;
    font-weight:800;
    color:#22c55e;
    margin:0;
    letter-spacing:-1px;
}
.result-label{
    color:#94a3b8;
    font-size:14px;
    margin-top:6px;
    font-weight:500;
}

.result-side{
    background: rgba(255,255,255,0.04);
    border:1px solid rgba(255,255,255,0.09);
    padding:26px;
    border-radius:20px;
    height:100%;
}
.result-side h3{
    color:#f1f5f9;
    margin:0 0 6px 0;
    font-size:19px;
    font-weight:700;
}
.result-side p{
    color:#94a3b8;
    margin:2px 0;
    font-size:13.5px;
}
.spec-chip{
    display:inline-block;
    background:rgba(99,102,241,0.15);
    color:#a5b4fc;
    border:1px solid rgba(99,102,241,0.3);
    padding:4px 10px;
    border-radius:8px;
    font-size:12px;
    font-weight:600;
    margin:3px 4px 0 0;
}

/* ---------- Divider ---------- */
hr{ border-color:rgba(255,255,255,0.08) !important; }

/* ---------- Sidebar ---------- */
section[data-testid="stSidebar"]{
    background:#0a0e1a;
    border-right:1px solid rgba(255,255,255,0.06);
}
section[data-testid="stSidebar"] .stMarkdown p{
    color:#94a3b8;
}

/* ---------- Footer ---------- */
.footer-note{
    text-align:center;
    color:#4b5567;
    font-size:12.5px;
    margin-top:30px;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:
    st.markdown("### 🚗 AI Predictor")
    st.markdown("---")
    st.success("✅ Model Loaded Successfully")

    st.markdown("#### About")
    st.write("This application predicts the market value of used cars using a trained Machine Learning model.")

    st.markdown("---")
    st.markdown("#### Model Info")
    st.info("**Algorithm:** Random Forest Regressor")
    st.info("**Training data:** 15,000+ listings")

    st.markdown("---")
    st.caption("Built with Streamlit · Powered by scikit-learn")

# -----------------------------
# HERO HEADER
# -----------------------------
st.markdown(
"""
<div class="hero-wrap">
    <div class="hero-badge">⚡ MACHINE LEARNING · LIVE PREDICTION</div>
    <div class="main-title">🚗 AI Used Car <span>Price Prediction</span></div>
    <div class="subtitle">Get an instant, data-driven estimate of your car's market value</div>
</div>
""",
unsafe_allow_html=True
)

st.write("")

# -----------------------------
# STATS
# -----------------------------
c1,c2,c3,c4=st.columns(4)
c1.metric("Accuracy","89.4%")
c2.metric("Model","Random Forest")
c3.metric("Dataset","15K+")
c4.metric("Status","🟢 Online")

st.write("")

# -----------------------------
# FORM
# -----------------------------
st.markdown('<div class="section-card">', unsafe_allow_html=True)

st.markdown(
    '<div class="section-title">📋 Car Information</div>'
    '<div class="section-sub">Fill in the details below to get an estimated price</div>',
    unsafe_allow_html=True
)

st.markdown('<div class="field-group-label">Identity</div>', unsafe_allow_html=True)
id_col1, id_col2, id_col3 = st.columns(3)
with id_col1:
    car_name = st.text_input("Car Name", placeholder="e.g. Alto")
with id_col2:
    brand = st.text_input("Brand", placeholder="e.g. Suzuki")
with id_col3:
    model_name = st.text_input("Model / Year", placeholder="e.g. 2019")

st.markdown('<div class="field-group-label">Usage & Ownership</div>', unsafe_allow_html=True)
use_col1, use_col2, use_col3 = st.columns(3)
with use_col1:
    vehicle_age = st.number_input("Vehicle Age (years)", 0, 30, 5)
with use_col2:
    km_driven = st.number_input("KM Driven", 0, 500000, 50000, step=1000)
with use_col3:
    seller_type = st.selectbox("Seller Type", ["Individual", "Dealer", "Trustmark Dealer"])

st.markdown('<div class="field-group-label">Technical Specifications</div>', unsafe_allow_html=True)
tech_col1, tech_col2, tech_col3 = st.columns(3)
with tech_col1:
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG", "LPG", "Electric"])
    transmission_type = st.selectbox("Transmission", ["Manual", "Automatic"])
with tech_col2:
    mileage = st.number_input("Mileage (km/l)", 0.0, 50.0, 18.0)
    engine = st.number_input("Engine (CC)", 500, 5000, 1200, step=50)
with tech_col3:
    max_power = st.number_input("Max Power (bhp)", 20.0, 500.0, 90.0)
    seats = st.number_input("Seats", 2, 10, 5)

st.write("")
predict = st.button("🚀 Predict Price", use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)  # close section-card

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

            with st.spinner("Analyzing car details and predicting price..."):
                prediction = model.predict(input_df)[0]

            st.write("")
            st.markdown('<div class="section-card">', unsafe_allow_html=True)
            st.markdown('<div class="section-title">💰 Prediction Result</div>', unsafe_allow_html=True)

            res_col1, res_col2 = st.columns([1.4, 1])

            with res_col1:
                st.markdown(
                    f"""
                    <div class="result-hero">
                        <p class="result-price">₹ {prediction:,.0f}</p>
                        <p class="result-label">Estimated Market Value</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            with res_col2:
                st.markdown(
                    f"""
                    <div class="result-side">
                        <h3>{brand} {car_name}</h3>
                        <p>Model: {model_name}</p>
                        <div style="margin-top:14px;">
                            <span class="spec-chip">🕒 {vehicle_age} yrs</span>
                            <span class="spec-chip">🛣️ {km_driven:,} km</span>
                            <span class="spec-chip">⛽ {fuel_type}</span>
                            <span class="spec-chip">⚙️ {transmission_type}</span>
                            <span class="spec-chip">🪑 {seats} seats</span>
                        </div>
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

st.markdown('<div class="footer-note">© 2026 AI Used Car Price Prediction · For estimation purposes only</div>', unsafe_allow_html=True)