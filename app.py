import streamlit as st

# Page config
st.set_page_config(page_title="My Streamlit App", page_icon="🤖", layout="wide")

# Horizontal Tabs
tabs = st.tabs(["🏠 Home", "📊 Predictor", "💬 Chatbot", "ℹ️ About"])

# Home Tab
with tabs[0]:
    st.title("🏠 Home")
    st.write("Welcome to the Streamlit App!")
    st.image("https://streamlit.io/images/brand/streamlit-mark-color.png", width=150)

# Predictor Tab
with tabs[1]:
    st.title("📊 Predictor")
    st.write("Enter your input data to get predictions.")
    user_input = st.number_input("Enter a value:", min_value=0.0, step=1.0)
    if st.button("Predict"):
        prediction = user_input * 2  # Example logic
        st.success(f"Predicted value: {prediction}")

# Chatbot Tab
with tabs[2]:
    st.title("💬 Chatbot")
    st.write("Ask me something!")
    user_message = st.text_input("You:")
    if user_message:
        bot_response = f"You said: {user_message}"  # Example chatbot logic
        st.info(bot_response)

# About Tab
with tabs[3]:
    st.title("ℹ️ About")
    st.write("""
    **App Name:** My Streamlit App  
    **Description:** This is a basic multi-tab Streamlit template.  
    **Author:** Your Name  
    """)
