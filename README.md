# 📊 Bank Marketing Dashboard — Interactive Data App

An interactive web dashboard built with **Python and Streamlit** that explores which customer profiles are most likely to subscribe to a term deposit, based on a Portuguese bank's marketing campaigns.

---

## 🔗 Live Demo

**[▶ Try the app here](https://bank-marketing-dashboard.streamlit.app/)**

*(Open the app, move the filters, and watch the metrics and charts update in real time.)*

---

## Overview

This project turns a static SQL analysis into a **live, interactive tool**. Instead of a fixed report, anyone can filter the data by job and age and instantly see how the conversion rate changes across customer segments — the kind of self-service dashboard a marketing or data team would actually use.

## Features

- **Interactive filters** (job type and age range) in the sidebar
- **Key metrics** that update live: total clients, subscribers, and conversion rate
- **Two interactive charts:** conversion rate by job and by age group
- Built on **45,211 real client records**

## Tech Stack

- **Python** · **Streamlit** (web app) · **pandas** (data) · **Plotly** (interactive charts)
- Data caching with `@st.cache_data` for performance

## Dataset

- **Source:** [UCI Bank Marketing dataset](https://archive.ics.uci.edu/dataset/222/bank+marketing) (`bank-full.csv`)
- 45,211 clients · 17 attributes · target: did the client subscribe a term deposit? (`yes` / `no`)

## Run Locally

```bash
# 1. Clone the repository
git clone https://github.com/gonzaloDomingo22/bank-marketing-dashboard.git
cd bank-marketing-dashboard

# 2. Install the dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run app.py
```

## Repository Structure

```
├── app.py             # The Streamlit application
├── bank-full.csv      # Dataset
├── requirements.txt   # Python dependencies
├── .gitignore         # Files excluded from the repo
└── README.md          # This file
```

---

*Author: Gonzalo Domingo Díaz-Malaguilla · [LinkedIn](https://www.linkedin.com/in/gonzalo-domingo-diaz-malaguilla-2280b4336) · [GitHub](https://github.com/gonzaloDomingo22)*
