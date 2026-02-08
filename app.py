import streamlit as st
import pandas as pd
import numpy as np
import joblib
st.set_page_config(
    page_title="Bengaluru Property Price Predictor",
    page_icon=print('\u0001F3E0'),
    layout="centered"
)
@st.cache_resource
def load_model():
    try:
        model = joblib.load("bengaluru_house_price_xgboost.pkl")
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        st.stop()

model = load_model()
st.title("🏠 Bengaluru Property Price Predictor")
st.markdown("""
Estimate the price of a residential property in Bangalore using our XGBoost model  
(trained on real estate data from Bengaluru).
""")
with st.form("property_form"):

    col1, col2 = st.columns(2)

    with col1:
        area_type = st.selectbox(
            "Area Type",
            options=["Super built-up  Area", "Built-up  Area", "Plot  Area", "Carpet  Area"]
        )

        total_sqft = st.number_input("Total Area (sqft)", min_value=300, max_value=10000, value=1200, step=50)

        bhk = st.slider("BHK (Bedrooms)", min_value=1, max_value=6, value=3)

    with col2:
        bath = st.slider("Bathrooms", min_value=1, max_value=8, value=2)

        balcony = st.slider("Balconies", min_value=0, max_value=4, value=1)

        availability = st.radio(
            "Availability",
            options=["Ready To Move", "Under Construction"],
            horizontal=True
        )
        availability_val = 1 if availability == "Ready To Move" else 0

    popular_locations = [
        "Whitefield", "Sarjapur  Road", "Electronic City", "Yelahanka",
        "Kanakpura Road", "Thanisandra", "JP Nagar", "Hebbal", "other"
    ]

    location = st.selectbox("Location", options=popular_locations)


    submitted = st.form_submit_button("Estimate Price", type="primary", use_container_width=True)
if submitted:
    # Prepare input DataFrame (must match training columns)
    input_data = pd.DataFrame([{
        "area_type": area_type,
        "availability": availability_val,
        "location": location,
        "total_sqft": total_sqft,
        "bath": bath,
        "balcony": balcony,
        "bhk": bhk
    }])

    try:
      
        prediction = model.predict(input_data)[0]

    
        if prediction < 1000:
            price_str = f"₹ {prediction:,.2f} lakhs"
        else:
            price_in_cr = prediction / 100
            price_str = f"₹ {price_in_cr:,.2f} Cr"

        st.success(f"**Estimated Price: {price_str}**")

    

    except Exception as e:
        st.error(f"Prediction error: {e}")
        st.info("Please check if all inputs are valid.")

st.info("This is an estimate only — actual prices may vary due to market conditions, negotiation, etc.")
st.markdown("---")
st.caption("Note: This is not financial advice — consult local experts for real transactions.")
