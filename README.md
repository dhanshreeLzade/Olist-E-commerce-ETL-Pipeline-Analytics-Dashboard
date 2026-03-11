# Olist E-commerce ETL Pipeline & Analytics Dashboard

This project demonstrates a complete **data engineering and analytics workflow**, transforming raw e-commerce data into meaningful business insights through an automated ETL pipeline and an interactive dashboard.

The system processes Olist e-commerce data to analyze **revenue trends, customer behavior, product performance, and city-wise sales insights**, enabling data-driven decision making.

---

# Project Objective

The objective of this project is to build an end-to-end pipeline that:
- Extracts raw data
- Cleans and transforms it
- Stores structured data
- Visualizes insights through an interactive dashboard

---

# Tech Stack

### Programming
- Python

### Data Processing
- Pandas
- NumPy
- SQLAlchemy

### Database
- SQLite

### Visualization
- Streamlit
- Plotly

### UI
- Custom CSS
- Dark themed dashboard

---

# Key Features

- Built a **Python ETL pipeline** to extract, transform, and load data
- Stored processed data in **SQLite database**
- Developed an **interactive dashboard using Streamlit**
- Created visualizations using **Plotly charts**

Dashboard Insights:
- Revenue Analysis
- Top Selling Products
- Top Customers
- City-wise Sales Performance
- Order Trends Over Time

---

# Project Architecture

```
Raw Dataset
     |
     v
Extract Data (Python)
     |
     v
Transform Data (Pandas)
     |
     v
Load Data (SQLite Database)
     |
     v
Streamlit Dashboard
     |
     v
Business Insights
```

---

# Project Structure

```
ecommerce_pipeline/
│
├── data/
│   ├── raw_data
│   └── processed_data
│
├── dashboard/
│   └── app.py
│
├── pipeline.py
├── requirements.txt
└── README.md
```

---

# How to Run the Project

### 1 Install Dependencies

```bash
pip install -r requirements.txt
```

### 2 Run ETL Pipeline

```bash
python pipeline.py
```

### 3 Run Dashboard

```bash
streamlit run dashboard/app.py
```

---

# Future Enhancements

- Real-time data streaming
- Automated ETL scheduling
- Predictive analytics
- AI-driven insights
- Interactive filtering
- Advanced dashboard visualizations

---

# Project Goal

To demonstrate a **complete data engineering project lifecycle** from:

**Raw Data → ETL Pipeline → Database → Interactive Dashboard → Business Insights**

---

# Author
**Dhanashree Zade**
---
# Tags

Data Engineering  
ETL Pipeline  
Python  
Streamlit  
Plotly  
Data Visualization  
Analytics  
Business Intelligence
