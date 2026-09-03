import streamlit as st
import pandas as pd
import plotly.express as px

# --- Page configuration (must be the first Streamlit command) ---
st.set_page_config(
    page_title="Bank Marketing Dashboard",
    page_icon="📊",
    layout="wide",
)

# --- Load the data (cached so it isn't reloaded on every interaction) ---
@st.cache_data
def load_data():
    return pd.read_csv("bank-full.csv", sep=";")

df = load_data()

# --- Header ---
st.title("📊 Bank Marketing Dashboard")
st.caption(
    "Interactive analysis of a Portuguese bank's marketing campaigns. "
    "Use the filters on the left to explore which customer profiles subscribe to a term deposit."
)

# --- Sidebar filters ---
st.sidebar.header("Filters")
jobs = sorted(df["job"].unique())
selected_jobs = st.sidebar.multiselect("Job", jobs, default=jobs)

min_age = int(df["age"].min())
max_age = int(df["age"].max())
age_range = st.sidebar.slider("Age range", min_age, max_age, (min_age, max_age))

# --- Apply filters ---
filtered = df[
    (df["job"].isin(selected_jobs))
    & (df["age"] >= age_range[0])
    & (df["age"] <= age_range[1])
]

# --- Key metrics ---
total_clients = filtered.shape[0]
subscribers = filtered[filtered["y"] == "yes"].shape[0]
conversion_rate = (subscribers / total_clients * 100) if total_clients > 0 else 0

col1, col2, col3 = st.columns(3)
col1.metric("Total clients", f"{total_clients:,}")
col2.metric("Subscribers", f"{subscribers:,}")
col3.metric("Conversion rate", f"{conversion_rate:.1f}%")

st.divider()

# --- Charts side by side ---
chart_col1, chart_col2 = st.columns(2)

with chart_col1:
    st.subheader("Conversion rate by job")
    by_job = (
        filtered.groupby("job")["y"]
        .apply(lambda s: (s == "yes").mean() * 100)
        .reset_index(name="conversion_rate")
        .sort_values("conversion_rate", ascending=False)
    )
    fig_job = px.bar(
        by_job, x="job", y="conversion_rate",
        labels={"job": "Job", "conversion_rate": "Conversion rate (%)"},
    )
    st.plotly_chart(fig_job, use_container_width=True)

with chart_col2:
    st.subheader("Conversion rate by age group")

    def age_group(age):
        if age < 30:
            return "Under 30"
        elif age < 45:
            return "30-44"
        elif age < 60:
            return "45-59"
        else:
            return "60+"

    chart_data = filtered.copy()
    chart_data["age_group"] = chart_data["age"].apply(age_group)
    by_age = (
        chart_data.groupby("age_group")["y"]
        .apply(lambda s: (s == "yes").mean() * 100)
        .reset_index(name="conversion_rate")
    )
    order = ["Under 30", "30-44", "45-59", "60+"]
    by_age["age_group"] = pd.Categorical(by_age["age_group"], categories=order, ordered=True)
    by_age = by_age.sort_values("age_group")
    fig_age = px.bar(
        by_age, x="age_group", y="conversion_rate",
        labels={"age_group": "Age group", "conversion_rate": "Conversion rate (%)"},
    )
    st.plotly_chart(fig_age, use_container_width=True)

st.divider()

# --- Data table ---
st.subheader("Filtered data")
st.dataframe(filtered.head(20))

# --- Footer ---
st.caption("Data source: UCI Bank Marketing dataset · Built with Streamlit")