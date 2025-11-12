import streamlit as st
import requests

st.title("AI Calculator")

API_URL = "http://127.0.0.1:8090/calculate"

user_query = st.text_input("Enter your question:")
if st.button("Calculate"):
    if user_query.strip() == "":
        st.warning(" Please enter a valid question.")
    else:
        with st.spinner(" Thinking..."):
            try:
                response = requests.post(API_URL, json={"question": user_query})
                if response.status_code == 200:
                    data = response.json()
                    if "error" in data:
                        st.error(f"Error: {data['error']}")
                    else:
                        st.success(" Done!")
                        st.markdown(f"**User Query:** {data['query']}")
                        st.markdown(f"**AI Response:** {data['response']}")
                else:
                    st.error(f"API Error: {response.status_code}")
            except Exception as e:
                st.error(f"Connection Error: {e}")
