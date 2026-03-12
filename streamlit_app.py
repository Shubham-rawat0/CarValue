import streamlit as st
import requests

st.set_page_config(
    page_title="CarValue AI — Precision Pricing",
    page_icon="🚗",
    layout="wide"
)

API_URL =(
    "https://carvalue-r1kw.onrender.com/predict" or
      "http://127.0.0.1:8000/predict")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:wght@300;400;500&display=swap');

*, *::before, *::after { box-sizing: border-box; }

html, body, .stApp {
    background: #0a0c10 !important;
    color: #e8e6e1 !important;
    font-family: 'DM Sans', sans-serif !important;
}

/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }
.block-container { padding: 0 !important; max-width: 100% !important; }

/* ---- HERO SECTION ---- */
.hero-wrap {
    position: relative;
    overflow: hidden;
    padding: 72px 60px 56px;
    background: #0a0c10;
    border-bottom: 1px solid #1e2028;
}

.hero-grid {
    position: absolute;
    inset: 0;
    background-image:
        linear-gradient(rgba(255,210,0,0.04) 1px, transparent 1px),
        linear-gradient(90deg, rgba(255,210,0,0.04) 1px, transparent 1px);
    background-size: 48px 48px;
    pointer-events: none;
}

.hero-glow {
    position: absolute;
    width: 600px; height: 300px;
    background: radial-gradient(ellipse, rgba(255,200,0,0.12) 0%, transparent 70%);
    top: -60px; left: 50%;
    transform: translateX(-50%);
    pointer-events: none;
}

.eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 8px;
    background: rgba(255,200,0,0.1);
    border: 1px solid rgba(255,200,0,0.25);
    border-radius: 100px;
    padding: 5px 14px;
    font-size: 11px;
    font-weight: 500;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: #ffd000;
    margin-bottom: 22px;
}

.eyebrow-dot {
    width: 6px; height: 6px;
    border-radius: 50%;
    background: #ffd000;
    animation: pulse-dot 2s ease-in-out infinite;
}

@keyframes pulse-dot {
    0%, 100% { opacity: 1; transform: scale(1); }
    50% { opacity: 0.4; transform: scale(0.7); }
}

.headline {
    font-family: 'Syne', sans-serif;
    font-size: clamp(36px, 5vw, 60px);
    font-weight: 800;
    line-height: 1.05;
    letter-spacing: -0.03em;
    margin: 0 0 16px;
    color: #f0ede6;
}

.headline-accent {
    color: #ffd000;
    position: relative;
    display: inline-block;
}

.headline-accent::after {
    content: '';
    position: absolute;
    bottom: 4px; left: 0; right: 0;
    height: 3px;
    background: linear-gradient(90deg, #ffd000, transparent);
    border-radius: 2px;
}

.subheadline {
    font-size: 17px;
    color: #6b7280;
    font-weight: 300;
    max-width: 520px;
    line-height: 1.65;
    margin: 0;
}

.trust-row {
    display: flex;
    gap: 32px;
    margin-top: 36px;
    flex-wrap: wrap;
}

.trust-item {
    display: flex;
    align-items: center;
    gap: 8px;
    font-size: 13px;
    color: #4b5563;
}

.trust-icon { color: #ffd000; font-size: 15px; }

/* ---- FORM SECTION ---- */
.form-section {
    padding: 56px 60px;
    background: #0a0c10;
}

.section-label {
    font-family: 'Syne', sans-serif;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #ffd000;
    margin-bottom: 28px;
    display: flex;
    align-items: center;
    gap: 10px;
}

.section-label::after {
    content: '';
    flex: 1;
    height: 1px;
    background: linear-gradient(90deg, #1e2028, transparent);
}

.field-card {
    background: #111318;
    border: 1px solid #1e2028;
    border-radius: 14px;
    padding: 28px 24px;
    margin-bottom: 16px;
    transition: border-color 0.25s ease;
    position: relative;
    overflow: hidden;
}

.field-card::before {
    content: '';
    position: absolute;
    top: 0; left: 0; right: 0;
    height: 2px;
    background: linear-gradient(90deg, #ffd000, transparent);
    opacity: 0;
    transition: opacity 0.3s;
}

.field-card:hover {
    border-color: rgba(255,208,0,0.3);
}

.field-card:hover::before { opacity: 1; }

.card-icon {
    font-size: 22px;
    margin-bottom: 12px;
    display: block;
}

.card-title {
    font-family: 'Syne', sans-serif;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: #374151;
    margin-bottom: 16px;
}

/* Streamlit widget overrides */
.stTextInput > label,
.stNumberInput > label,
.stSelectbox > label {
    font-size: 12px !important;
    font-weight: 500 !important;
    color: #6b7280 !important;
    letter-spacing: 0.04em !important;
    text-transform: uppercase !important;
    margin-bottom: 4px !important;
}

.stTextInput input,
.stNumberInput input {
    background: #0d0f14 !important;
    border: 1px solid #1e2028 !important;
    border-radius: 8px !important;
    color: #e8e6e1 !important;
    font-family: 'DM Sans', sans-serif !important;
    font-size: 15px !important;
    padding: 10px 14px !important;
    transition: border-color 0.2s !important;
}

.stTextInput input:focus,
.stNumberInput input:focus {
    border-color: #ffd000 !important;
    box-shadow: 0 0 0 3px rgba(255,208,0,0.08) !important;
    outline: none !important;
}

.stSelectbox > div > div {
    background: #0d0f14 !important;
    border: 1px solid #1e2028 !important;
    border-radius: 8px !important;
    color: #e8e6e1 !important;
}

/* ---- DIVIDER ---- */
.divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, #1e2028 20%, #1e2028 80%, transparent);
    margin: 0 60px;
}

/* ---- PREDICT BUTTON ---- */
.stButton > button {
    width: 100% !important;
    background: linear-gradient(135deg, #ffd000 0%, #ffb300 100%) !important;
    color: #0a0c10 !important;
    border: none !important;
    border-radius: 12px !important;
    font-family: 'Syne', sans-serif !important;
    font-size: 15px !important;
    font-weight: 700 !important;
    letter-spacing: 0.04em !important;
    padding: 16px 32px !important;
    cursor: pointer !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 4px 24px rgba(255,208,0,0.25) !important;
    text-transform: uppercase !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 32px rgba(255,208,0,0.4) !important;
    background: linear-gradient(135deg, #ffe033 0%, #ffc200 100%) !important;
}

.stButton > button:active {
    transform: translateY(0) !important;
}

/* ---- RESULT CARD ---- */
.result-outer {
    padding: 40px 60px 60px;
    background: #0a0c10;
}

.result-card {
    background: #111318;
    border: 1px solid rgba(255,208,0,0.2);
    border-radius: 20px;
    padding: 48px;
    text-align: center;
    position: relative;
    overflow: hidden;
}

.result-card::before {
    content: '';
    position: absolute;
    inset: 0;
    background: radial-gradient(ellipse at 50% 0%, rgba(255,208,0,0.06) 0%, transparent 60%);
    pointer-events: none;
}

.result-label {
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.18em;
    text-transform: uppercase;
    color: #4b5563;
    margin-bottom: 12px;
}

.result-price {
    font-family: 'Syne', sans-serif;
    font-size: clamp(40px, 6vw, 72px);
    font-weight: 800;
    color: #ffd000;
    line-height: 1;
    margin-bottom: 8px;
    letter-spacing: -0.03em;
}

.result-currency {
    font-size: 0.4em;
    vertical-align: super;
    margin-right: 4px;
    color: #ffb300;
}

.result-unit {
    font-size: 18px;
    color: #6b7280;
    font-weight: 300;
    margin-bottom: 24px;
}

.result-badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(34,197,94,0.1);
    border: 1px solid rgba(34,197,94,0.2);
    border-radius: 100px;
    padding: 6px 16px;
    font-size: 12px;
    color: #4ade80;
    font-weight: 500;
}

/* ---- TOGGLE ---- */
.stCheckbox, .stToggle { display: none !important; }

/* Error styling */
.stAlert {
    background: rgba(239,68,68,0.08) !important;
    border: 1px solid rgba(239,68,68,0.2) !important;
    border-radius: 10px !important;
    color: #f87171 !important;
}
</style>
""", unsafe_allow_html=True)


st.markdown("""
<div class="hero-wrap">
    <div class="hero-grid"></div>
    <div class="hero-glow"></div>
    <h1 class="headline">
        Find <span class="headline-accent">Accurate</span><br>
        Car Pricing — Instantly
    </h1>
    <p class="subheadline">
        Get a data-driven resale valuation for any car in seconds. 
        Our ML model analyses market trends, condition factors, and 
        historical sales to deliver a precise price estimate.
    </p>
    <div class="trust-row">
        <div class="trust-item"><span class="trust-icon">⚡</span> Real-time predictions</div>
        <div class="trust-item"><span class="trust-icon">🎯</span> High accuracy model</div>
        <div class="trust-item"><span class="trust-icon">🔒</span> No data stored</div>
        <div class="trust-item"><span class="trust-icon">🇮🇳</span> India market calibrated</div>
    </div>
</div>
""", unsafe_allow_html=True)


st.markdown('<div class="form-section">', unsafe_allow_html=True)
st.markdown('<div class="section-label">Vehicle Details</div>', unsafe_allow_html=True)

col1, col2, col3 = st.columns([1, 1, 1], gap="large")

with col1:
    st.markdown('<div class="field-card"><span class="card-icon">🚘</span><div class="card-title">Car Identity</div>', unsafe_allow_html=True)
    car_name = st.text_input("Car Name", "swift", label_visibility="visible")
    year = st.number_input("Manufacturing Year", 1990, 2026, 2014)
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="field-card"><span class="card-icon">📊</span><div class="card-title">Usage & Value</div>', unsafe_allow_html=True)
    present_price = st.number_input("Showroom Price (₹ Lakhs)", 0.0, 100.0, 5.59)
    kms_driven = st.number_input("Odometer (km)", 0, 500000, 40000)
    st.markdown('</div>', unsafe_allow_html=True)

with col3:
    st.markdown('<div class="field-card"><span class="card-icon">⚙️</span><div class="card-title">Specifications</div>', unsafe_allow_html=True)
    fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
    seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
    transmission = st.selectbox("Transmission", ["Manual", "Automatic"])
    owner = st.selectbox("Previous Owners", [0, 1, 3])
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)  # close form-section


st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

_, btn_col, _ = st.columns([1.5, 1, 1.5])
with btn_col:
    predict = st.button("Get Valuation")

st.markdown("<br>", unsafe_allow_html=True)


payload = {
    "Car_Name": car_name,
    "Year": year,
    "Present_Price": present_price,
    "Kms_Driven": kms_driven,
    "Fuel_Type": fuel_type,
    "Seller_Type": seller_type,
    "Transmission": transmission,
    "Owner": owner
}


if predict:
    try:
        res = requests.post(API_URL, json=payload)
        if res.status_code == 200:
            data = res.json()
            pred = data.get("prediction", data.get("predicted_price"))
            st.markdown(f"""
            <div class="result-outer">
                <div class="result-card">
                    <div class="result-label">Estimated Resale Value</div>
                    <div class="result-price">
                        <span class="result-currency">₹</span>{pred:.2f}
                    </div>
                    <div class="result-unit">Lakhs</div>
                </div>
            </div>
            <script>
                setTimeout(() => {{
                    document.querySelector('.result-outer').scrollIntoView({{ behavior: 'smooth', block: 'center' }});
                }}, 100);
            </script>
            """, unsafe_allow_html=True)
        else:
            st.error(f"API returned an error (status {res.status_code}). Please check your backend.")
    except requests.exceptions.ConnectionError:
        st.error("Cannot connect to FastAPI backend. Make sure it's running at http://127.0.0.1:8000")
    except Exception as e:
        st.error(f"Unexpected error: {e}")