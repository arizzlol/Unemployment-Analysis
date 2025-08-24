import streamlit as st
import streamlit_option_menu as option_menu
from streamlit_lottie import st_lottie
import json
import streamlit.components.v1 as components
from dashboard import dashboard_page
from analyzer import analyzer_page

st.set_page_config(page_title="Global Unemployment Analysis", page_icon="🌐", layout="centered")

# -------- HOMEPAGE CONTENT FUNCTION --------
def homepage():
    st.markdown(
        """
        <style>
        .stApp {
            font-family: 'Funnel Display SemiBold', sans-serif;
            background-color: #121212;
            color: #e0e0e0;
            background-color: #f0f2f5;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <h1 style="
            text-align: center;
            background: linear-gradient(90deg, #2193b0 0%, #6dd5ed 50%, #56ab2f 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            font-family: 'Funnel Display SemiBold', sans-serif;
            padding: 20px 0;
        ">
        Global Unemployment Analysis
        </h1>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <style>
        .stApp {
            background-image: linear-gradient(rgba(0,0,0,0.6), rgba(0,0,0,0.6)), 
                              url("https://wallpaperbat.com/img/879351-analysis-wallpaper-top-free-analysis-background.jpg");
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        """
        <h3 style="text-align: center;">
            Welcome to the Global Unemployment Analysis Dashboard! 🌍📊
        </h3>
        """,
        unsafe_allow_html=True
    )
    st.write("This dashboard provides insights into global unemployment trends, analyzing data from various countries and regions to understand the factors affecting employment rates.")
    st.write("Use the navigation menu on the left to explore different sections of the dashboard, including data visualizations, country-specific analyses, and more.")

    # ----- COLUMNS CONTENT -----
    col1, col2, col3 = st.columns([1, 1, 1])

    with col1:
        st.header("Welcome to Our Dashboard")
        json1 = "https://lottie.host/02c12a6c-dead-4c3e-a233-0b5e6b06453d/4S1l8e9JXV.json"
        components.html(f"""
        <div id="lottie" style="height: 200px; background: transparent; margin: auto;"></div>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.10.2/lottie.min.js"></script>
        <script>
            lottie.loadAnimation({{
                container: document.getElementById('lottie'),
                renderer: 'svg',
                loop: true,
                autoplay: true,
                path: '{json1}',
                rendererSettings: {{
                    preserveAspectRatio: 'xMidYMid meet',
                    progressiveLoad: true,
                    clearCanvas: true
                }}
            }});
        </script>
        """, height=200)
        st.write("This website provides insights into global unemployment trends.")

    with col2:
        st.header("About Us")
        json2 = "https://lottie.host/bcf3116a-d3a1-4316-b1a3-1848000225f8/dcu5socJLL.json"
        components.html(f"""
        <div id="lottie" style=" height: 300px; background: transparent; margin: auto;"></div>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.10.2/lottie.min.js"></script>
        <script>
            lottie.loadAnimation({{
                container: document.getElementById('lottie'),
                renderer: 'svg',
                loop: true,
                autoplay: true,
                path: '{json2}',
                rendererSettings: {{
                    preserveAspectRatio: 'xMidYMid meet',
                    progressiveLoad: true,
                    clearCanvas: true
                }}
            }});
        </script>
        """, height=300)
        st.write("We are dedicated to analyzing and presenting data on unemployment across different countries and regions.")

    with col3:
        st.header("Contact Us")
        json3 = "https://lottie.host/ccb5e690-be42-48b4-a770-58765f7e8a60/pm5kmrEFLJ.json"
        components.html(f"""
        <div id="lottie" style="height: 200px; background: transparent; margin: auto;"></div>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/lottie-web/5.10.2/lottie.min.js"></script>
        <script>
            lottie.loadAnimation({{
                container: document.getElementById('lottie'),
                renderer: 'svg',
                loop: true,
                autoplay: true,
                path: '{json3}',
                rendererSettings: {{
                    preserveAspectRatio: 'xMidYMid meet',
                    progressiveLoad: true,
                    clearCanvas: true
                }}
            }});
        </script>
        """, height=200)
        st.write("For inquiries, please reach out to us at: info@jobanalysis.com")


# -------- SIDEBAR --------
with st.sidebar:
    st.markdown("""
                <h2><center>🌐 Menu</center></h2>
    """, unsafe_allow_html=True)
    menu_options = ["Homepage", "Global Analysis Dashboard", "Country Employment Analyzer"]
    selected = option_menu.option_menu(
        menu_title=None,
        options=menu_options,
        icons=["house", "bar-chart", "globe"],
        menu_icon="cast",
        default_index=0,
        orientation="vertical",
        styles={
            "container": {"padding": "20px 10px", "background": "linear-gradient(135deg, #1a237e 0%, #2193b0 100%)", "border-radius": "15px"},
            "icon": {"color": "#fff", "font-size": "1.3rem"},
            "nav-link": {"font-size": "1.05rem", "color": "#fff", "background": "rgba(33,147,176,0.25)", "border-radius": "8px", "margin": "8px 0"},
            "nav-link-selected": {"background": "#56ab2f", "color": "#f0f2f5"},
        }
    )
    st.markdown("---")
    st.markdown(
        "<div style='text-align:center; font-size:1.1rem; font-weight:bold; background:linear-gradient(90deg, #2193b0 0%, #6dd5ed 50%, #56ab2f 100%); -webkit-background-clip:text; -webkit-text-fill-color:transparent;'>Crafted by <b>Arihant 🤖</b></div>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<div style='text-align:center; margin-top:10px;'><a href='https://github.com/arizzlol' target='_blank' style='color:#fff; background:rgba(33,147,176,0.25); border-radius:8px; padding:6px 12px; text-decoration:none; font-weight:600;'>🐙 My GitHub</a></div>",
        unsafe_allow_html=True
    )

# -------- PAGE ROUTING --------
if selected == "Homepage":
    homepage()
elif selected == "Global Analysis Dashboard":
    dashboard_page()
elif selected == "Country Employment Analyzer":
    analyzer_page()
