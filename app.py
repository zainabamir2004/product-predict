import streamlit as st
import pickle
import numpy as np

# 1. Load the model
model = pickle.load(open("model.pkl", "rb"))

# 2. Page Config
st.set_page_config(page_title="Product Predictor", page_icon="🛒")

# 3. Custom CSS for Visuals & Mobile Visibility
st.markdown("""
    <style>
    .stApp {
        background-color: #f4f7f6;
    }
    /* Fix for mobile text visibility */
    label, .stSubheader, p {
        color: #2c3e50 !important;
        font-weight: 500 !important;
    }
    div.stButton > button:first-child {
        background: linear-gradient(to right, #00b4db, #0083b0);
        color: white;
        border: none;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-weight: bold;
    }
    /* Responsive Header Text */
    .main-title {
        color: white; 
        text-align: center; 
        font-size: 28px; /* Reduced size to fit one line */
        margin: 0;
        font-weight: bold;
    }
    @media (max-width: 600px) {
        .main-title {
            font-size: 20px; /* Even smaller for phones */
        }
    }
    </style>
    """, unsafe_allow_html=True)

# 4. Updated HTML Header (Smaller Font)
st.markdown("""
    <div style="background: #2c3e50; padding: 20px; border-radius: 15px; margin-bottom: 25px;">
        <h1 class="main-title">🛒 Product Recommendation System</h1>
        <p style="color: #ecf0f1; text-align: center; margin: 5px 0 0 0; font-size: 14px;">Learning Consumer Behaviour</p>
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
if st.button("Generate AI Prediction"):
    features = np.array([[user_id, product_id, times_bought, recency, prod_pop]])
    prediction = model.predict(features)
    
    if prediction[0] == 1:
        st.balloons()
        st.markdown("""
            <div style="background-color: #d4edda; border-left: 10px solid #28a745; padding: 20px; border-radius: 10px;">
                <h2 style="color: #155724; margin: 0; font-size: 18px;">✅ Result: High Reorder Probability</h2>
                <p style="color: #155724;">This user is very likely to purchase this product again.</p>
            </div>
            """, unsafe_allow_html=True)
    else:
        st.markdown("""
            <div style="background-color: #f8d7da; border-left: 10px solid #dc3545; padding: 20px; border-radius: 10px;">
                <h2 style="color: #721c24; margin: 0; font-size: 18px;">❌ Result: Low Reorder Probability</h2>
                <p style="color: #721c24;">This user is unlikely to buy this specific product in their next order.</p>
            </div>
            """, unsafe_allow_html=True)