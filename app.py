import streamlit as st
import pickle
import numpy as np

# Load the saved model
model = pickle.load(open("model.pkl", "rb"))

st.title("🛒 Product Recommendation System")
st.write("Enter details below to predict if a user will reorder a product.")

# We need 5 inputs because the model was trained on 5 columns
# 1. User ID
user_id = st.number_input("User ID (e.g., 1)", min_value=1, value=1)
# 2. Product ID
product_id = st.number_input("Product ID (e.g., 100)", min_value=1, value=100)
# 3. Times Bought (Frequency)
times_bought = st.number_input("Times User Bought Product", min_value=0, value=5)
# 4. Recency (How many orders ago)
recency = st.number_input("Recency (How many orders ago)", min_value=0, value=1)
# 5. Product Popularity
prod_pop = st.number_input("Product Popularity (Global Sales)", min_value=0, value=500)

if st.button("Predict"):
    # The order MUST be: user_id, product_id, times_bought, recency, product_popularity
    features = np.array([[user_id, product_id, times_bought, recency, prod_pop]])
    
    prediction = model.predict(features)
    
    if prediction[0] == 1:
        st.success("✅ The user is LIKELY to buy this again!")
    else:
        st.error("❌ The user is UNLIKELY to buy this again.")