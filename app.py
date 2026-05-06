import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Advanced Page Config
st.set_page_config(
    page_title="Pro Film Production Dashboard",
    page_icon="🎬",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for Dark-themed Sidebar and better design
st.markdown("""
    <style>
    [data-testid="stSidebar"] {
        background-color: #111827;
        color: white;
    }
    .stMetric {
        background-color: #f8fafc;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #e2e8f0;
    }
    </style>
    """, unsafe_allow_html=True)

# 2. Data Initialization
if 'movies_df' not in st.session_state:
    data = {
        "Title": ["Avatar", "Titanic", "The Avengers", "Jurassic Park", "Inception", "Interstellar", "Pulp Fiction"],
        "Director": ["James Cameron", "James Cameron", "Joss Whedon", "Steven Spielberg", "Christopher Nolan", "Christopher Nolan", "Quentin Tarantino"],
        "Year": [2009, 1997, 2012, 1993, 2010, 2014, 1994],
        "Genre": ["Sci-Fi", "Romance", "Action", "Adventure", "Sci-Fi", "Sci-Fi", "Crime"],
        "Budget ($M)": [237, 200, 220, 63, 160, 165, 8],
        "Revenue ($M)": [2923, 2264, 1518, 1033, 836, 701, 213]
    }
    df = pd.DataFrame(data)
    df['ROI (%)'] = ((df['Revenue ($M)'] - df['Budget ($M)']) / df['Budget ($M)'] * 100).round(1)
    st.session_state.movies_df = df

# --- SIDEBAR: Controls & Inputs ---
with st.sidebar:
    st.title("🎥 Studio Control")
    st.markdown("Add new projects to the pipeline below.")

    with st.form("movie_form"):
        new_title = st.text_input("Project Title 📝")
        new_director = st.text_input("Director 👤")
        new_year = st.number_input("Release Year", 1900, 2030, 2024)
        new_genre = st.selectbox("Genre 🎭", ["Action", "Sci-Fi", "Drama", "Comedy", "Horror", "Adventure", "Crime"])
        new_budget = st.number_input("Budget ($M) 💰", min_value=1)
        new_revenue = st.number_input("Revenue ($M) 📈", min_value=0)

        if st.form_submit_button("Submit to Database ✨"):
            if new_title and new_director:
                new_roi = round(((new_revenue - new_budget) / new_budget * 100), 1)
                new_entry = pd.DataFrame({
                    "Title": [new_title], "Director": [new_director], "Year": [new_year],
                    "Genre": [new_genre], "Budget ($M)": [new_budget],
                    "Revenue ($M)": [new_revenue], "ROI (%)": [new_roi]
                })
                st.session_state.movies_df = pd.concat([st.session_state.movies_df, new_entry], ignore_index=True)
                st.success("Database Updated!")

    # Download Feature
    st.markdown("---")
    csv = st.session_state.movies_df.to_csv(index=False).encode('utf-8')
    st.download_button(
        label="📥 Download Data as CSV",
        data=csv,
        file_name='film_production_data.csv',
        mime='text/csv',
    )

# --- MAIN DASHBOARD ---
st.title("🎬 Global Film Production Dashboard")

# 3. Statistics Cards (Metrics)
st.subheader("Key Performance Indicators (KPI)")
m1, m2, m3, m4 = st.columns(4)

total_rev = st.session_state.movies_df["Revenue ($M)"].sum()
avg_roi = st.session_state.movies_df["ROI (%)"].mean()
max_budget = st.session_state.movies_df["Budget ($M)"].max()
movie_count = len(st.session_state.movies_df)

m1.metric("Total Revenue", f"${total_rev:,.0f}M", "Global")
m2.metric("Average ROI", f"{avg_roi:.1f}%", "Profitability")
m3.metric("Highest Budget", f"${max_budget}M", "Investment")
m4.metric("Total Projects", movie_count, "Database Size")

st.markdown("---")

# 4. Filters & Search
c1, c2 = st.columns([2, 1])
with c1:
    search = st.text_input("🔍 Search by Title or Director", "")
with c2:
    years = st.slider("Filter by Year", 1990, 2030, (1990, 2030))

filtered_df = st.session_state.movies_df[
    (st.session_state.movies_df['Year'] >= years[0]) &
    (st.session_state.movies_df['Year'] <= years[1])
]
if search:
    filtered_df = filtered_df[filtered_df['Title'].str.contains(search, case=False) |
                              filtered_df['Director'].str.contains(search, case=False)]

# 5. Visualizations
st.subheader("📊 Market Analysis")
tab1, tab2 = st.tabs(["Financials", "Genre Insights"])

with tab1:
    fig_bar = px.bar(filtered_df, x="Title", y=["Budget ($M)", "Revenue ($M)"],
                     barmode="group", title="Budget vs Revenue Comparison",
                     template="plotly_white", color_discrete_sequence=['#ef4444', '#10b981'])
    st.plotly_chart(fig_bar, use_container_width=True)

with tab2:
    fig_pie = px.pie(filtered_df, names="Genre", values="Revenue ($M)",
                     hole=0.4, title="Revenue Share by Genre")
    st.plotly_chart(fig_pie, use_container_width=True)

# 6. Trend Chart
st.subheader("📈 Profitability Trends (ROI)")
fig_line = px.line(filtered_df.sort_values("Year"), x="Year", y="ROI (%)",
                   color="Genre", hover_name="Title", markers=True)
st.plotly_chart(fig_line, use_container_width=True)

st.balloons()
