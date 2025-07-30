import streamlit as st
st.set_page_config(page_title="Global Unemployment Analysis", page_icon="🌐", layout="centered")
st.markdown(
    """
    <h1 style="text-align: center;">Global Unemployment Analysis</h1>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <div style="text-align: center;">
        <img src="https://etimg.etb2bimg.com/photo/87034270.cms" width="400" alt="Global Unemployment Trends">
        <p><em>Global Unemployment Trends</em></p>
    </div>
    """,
    unsafe_allow_html=True
)
col1, col2, col3 = st.columns([2, 2, 2])
with col1:
    st.header("Welcome to Our Website")
    st.write("This website provides insights into global unemployment trends.")
with col2:
    st.header("About Us")
    st.write("We are dedicated to analyzing and presenting data on unemployment across different countries and regions.")
with col3:
    st.header("Contact Us")
    st.write("For inquiries, please reach out to us at: info@jobanalysis.com")
st.write("This project is a comprehensive analysis of healthcare data, focusing on various aspects such as patient demographics, treatment outcomes, and healthcare costs.")
st.write("****Name: Arihant Bhan****")
st.write("****Roll No: 2301732****")
st.write("****Branch: Btech ECE****")
