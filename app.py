import streamlit as st
import pickle
import numpy as np

# 1. Load the model
model = pickle.load(open("model.pkl", "rb"))

# 2. Page Config
st.set_page_config(page_title="Product Predictor", page_icon="🛒")

# 3. High-Contrast CSS for Mobile Visibility & Font Balancing
st.markdown("""
    <style>
    /* Force main app background */
    .stApp {
        background-color: #f4f7f6 !important;
    }
    
    /* Header Box Styling */
    .header-container {
        background-color: #2c3e50; 
        padding: 15px; 
        border-radius: 12px; 
        margin-bottom: 20px;
        text-align: center;
    }
    
    .main-title {
        color: #ffffff !important; 
        font-size: 28px !important; /* Made a bit bigger */
        margin: 0 !important;
        font-weight: bold !important;
    }
    
    .sub-title {
        color: #ecf0f1 !important; 
        font-size: 13px !important;
    }

    /* CUSTOMER DATA INPUT HEADING - Made smaller */
    h3, .stSubheader {
        color: #1a2a3a !important;
        font-size: 18px !important; /* Reduced from default */
        font-weight: 700 !important;
        margin-top: 10px !important;
    }

    /* Input labels visibility */
    label p {
        color: #1a2a3a !important;
        font-weight: bold !important;
        font-size: 15px !important;
    }

    /* Input box styling */
    .stNumberInput div div {
        background-color: #ffffff !important;
        border: 1px solid #d1d8e0 !important;
    }

    @media (max-width: 600px) {
        .main-title {
            font-size: 22px !important; /* Adjusted for mobile */
        }
        h3, .stSubheader {
            font-size: 16px !important;
        }
    }
    </style>
    """, unsafe_allow_html=True)

# 4. Refined Header
st.markdown("""
    <div class="header-container">
        <h1 class="main-title">🛒 Customer Purchase Predictor</h1>
        <p class="sub-title">Learning Consumer Behaviour</p>
    </div>
    """, unsafe_allow_html=True)

# 5. Input Layout
st.subheader("📊 Customer Data Input")
with st.container():
    col1, col2 = st.columns(2)
    with col1:
        user_id = st.number_input("👤 User ID", min_value=1, value=1)
        product_id = st.number_input("📦 Product ID", min_value=1, value=1)
        times_bought = st.number_input("📈 Times Previously Bought", min_value=0, value=5)
    with col2:
        recency = st.number_input("🕒 Recency (Orders Ago)", min_value=0, value=1)
        prod_pop = st.number_input("🔥 Product Popularity (Global Sales)", min_value=0, value=500)

st.markdown("---")

# 6. Prediction Logic
if st.button("Predict", use_container_width=True):
    features = np.array([[user_id, product_id, times_bought, recency, prod_pop]])
    prediction = model.predict(features)
    
    if prediction[0] == 1:
        st.balloons()
        st.success("### ✅ Result: High Reorder Probability")
        st.write("This user is very likely to purchase this product again.")
    else:
        st.error("### ❌ Result: Low Reorder Probability")
        st.write("This user is unlikely to buy this specific product in their next order.")