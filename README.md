
# 🌐 Global Unemployment Analysis Dashboard  

An interactive **Streamlit web application** for analyzing and visualizing **global unemployment trends** using data from multiple countries, age groups, and genders.  

This project provides comparative analysis, trend exploration, demographic breakdowns, and visual insights into unemployment patterns worldwide.  

---

## 📂 Project Structure  

```
├── app_hmpg.py                  # Main entry point of the Streamlit app
├── dashboard.py                 # Global analysis dashboard (world map, country comparisons, youth vs. adult unemployment)
├── analyzer.py                  # Country-specific analyzer with multiple visualization options
├── global_unemployment_data.csv # Dataset containing global unemployment statistics
├── requirements.txt             # Python dependencies for the project
```

---

## 🚀 Features  

### **Homepage (`app_hmpg.py`)**  
- Navigation menu (Homepage, Global Dashboard, Country Analyzer).  
- Welcoming UI with animations (Lottie).  
- Contact and About section.  

### **Global Analysis Dashboard (`dashboard.py`)**  
- Interactive **world map** showing unemployment by country.  
- **Country-to-country comparison** by sex and age groups.  
- **Youth vs. Adult unemployment** scatter plot for structural insights.  
- Powered by **Plotly** for rich interactivity.  

### **Country Employment Analyzer (`analyzer.py`)**  
- **Unemployment trend over time** for a selected country, sex, and age group.  
- **Comparison of top N countries** by unemployment rate in a given year.  
- **Breakdown by sex and age group** for specific countries.  
- **Distribution histograms** for unemployment rates across all countries.  
- **Correlation heatmap** between unemployment rates over different years.  

---

## 🛠️ Requirements  

Install dependencies from `requirements.txt`:  

```bash
pip install -r requirements.txt
```

---

## ▶️ How to Run  

1. Clone the repository:  
   ```bash
   git clone https://github.com/<your-username>/global-unemployment-dashboard.git
   cd global-unemployment-dashboard
   ```

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:  
   ```bash
   streamlit run app_hmpg.py
   ```

4. Open in browser at: [http://localhost:8501](http://localhost:8501)  

---

## 📊 Dataset  

- **File**: `global_unemployment_data.csv`  
- Contains yearly unemployment rates (2014–2024) across multiple countries, segmented by:  
  - **Country Name**  
  - **Sex** (Male/Female)  
  - **Age Groups** (15–24, 25+, etc.)  
  - **Indicator Name / Categories**  

---

## ✨ Future Enhancements  

- Add **forecasting models** for unemployment prediction.  
- More **filters and demographic breakdowns**.  
- Deploy to **Streamlit Cloud / Hugging Face Spaces** for public access.  

---

## 👨‍💻 Author  

Crafted with 💻 by **Arihant**  
- GitHub: [@arizzlol](https://github.com/arizzlol)  
