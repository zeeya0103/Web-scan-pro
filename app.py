import streamlit as st

st.title("WebScanPro – Web Security Scanner")

st.write("Select a module to run:")

option = st.selectbox(
    "Choose Testing Module",
    ["SQL Injection Test", "XSS Test", "IDOR Test"]
)

url = st.text_input("Enter URL")

if st.button("Run Test"):
    if option == "SQL Injection Test":
        st.success("SQL Injection Test Completed (sample output)")
    elif option == "XSS Test":
        st.success("XSS Test Completed (sample output)")
    elif option == "IDOR Test":
        st.success("IDOR Test Completed (sample output)")