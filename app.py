import streamlit as st
import pickle
import numpy as np

# 1. Load the model
model = pickle.load(open("model.pkl", "rb"))

# 2. Page Config
st.set_page_config(page_title="Product Predictor", page_icon="🛒")

# 3. Enhanced CSS for Visibility & Layout
st.markdown("""
    <style>
    /* Force main background color */
    .stApp {
        background-color: #f4f7f6;
    }
    
    /* Fix for title text blending with background */
    .header-container {
        background-color: #2c3e50; 
        padding: 15px; 
        border-radius: 12px; 
        margin-bottom: 20px;
        text-align: center;
    }
    
    .main-title {
        color: #ffffff !important; /* Force Pure White */
        font-size: 24px !important; /* Smaller size to stay on one line */
        margin: 0 !important;
        font-weight: bold !important;
        line-height: 1.2 !important;
    }
    
    .sub-title {
        color: #ecf0f1 !important; /* Light gray-white */
        font-size: 14px !important;
        margin-top: 5px !important;
    }

    /* Mobile Responsive Font Size */
    @media (max-width: 600px) {
        .main-title {
            font-size: 18px !important;
        }
    }

    /* Ensure labels are visible on phone */
    label p {
        color: #2c3e50 !important;
        font-weight: bold !important;
    }
    </style>
    """, unsafe_allow_html=True)

# 4. Refined Header
st.markdown("""
    <div class="header-container">
        <h1 class="main-title">🛒 Product Recommendation System</h1>
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