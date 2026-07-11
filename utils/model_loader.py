import joblib
import streamlit as st
from pathlib import Path

@st.cache_resource
def load_model():
    model_path = Path("backend/models/used_car_price_model.joblib")

    if not model_path.exists():
        st.error(f"Model not found: {model_path}")
        st.stop()

    model = joblib.load(model_path)
    return model