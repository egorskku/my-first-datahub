# 🎬 Pro Film Production Dashboard

A high-concept Streamlit application designed for action-oriented film data management and financial visualization. This dashboard provides studio executives with real-time insights into ROI, revenue shares, and production budget comparisons.

---

## 🚀 Features

* **KPI Metrics**: Instant tracking of Total Revenue, Average ROI, Highest Investment, and Total Project count.
* **Interactive Database**: Add new film projects via a custom sidebar form with automatic ROI calculation.
* **Dynamic Visualizations**: 
    * **Financials**: Grouped bar charts comparing Budget vs. Revenue.
    * **Genre Insights**: Donut charts showing revenue distribution across genres.
    * **Trend Analysis**: Interactive line charts tracking profitability trends over time.
* **Advanced Filtering**: Search by title or director and filter by release year using a dual-ended slider.
* **Data Portability**: Export the current production database directly to a CSV file.

## 🛠️ Tech Stack

* **Python**: Core logic and data processing.
* **Streamlit**: Web interface and dashboard framework.
* **Pandas**: Data manipulation and DataFrame management.
* **Plotly Express**: Interactive, high-fidelity data visualizations.

## 📦 Installation & Setup

1.  **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/pro-film-dashboard.git
    cd pro-film-dashboard
    ```

2.  **Install dependencies**:
    ```bash
    pip install streamlit pandas plotly
    ```

3.  **Run the application**:
    ```bash
    streamlit run app.py
    ```

## 📂 Project Structure

* `app.py`: The main application script containing the Streamlit UI logic, custom CSS, and data visualizations.
* `README.md`: Project documentation.

## 💡 Usage

Once the dashboard is running:
1.  Use the **Studio Control** sidebar to enter a project title, director, budget, and revenue.
2.  Click **Submit to Database** to update the dashboard instantly.
3.  Analyze market trends using the **Market Analysis** tabs.
4.  Download the full dataset using the **Download Data** button for external reporting.
