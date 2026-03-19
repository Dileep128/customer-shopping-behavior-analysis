# 🛍️ Customer Shopping Behavior Analysis

## 📌 Project Overview
This project analyzes customer shopping behavior using transactional data to uncover insights into purchasing patterns, customer segments, and revenue drivers. The goal is to help businesses optimize marketing strategies, improve customer engagement, and drive sales growth.

This is an end-to-end data analytics project covering data cleaning, modeling, SQL-based analysis, and interactive dashboard development.

---

## ❓ Business Problem
A retail company wants to understand changing customer purchasing patterns across demographics, product categories, and channels to improve sales and customer loyalty.

Key question:
> How can consumer shopping data be leveraged to identify trends, improve engagement, and optimize marketing strategies?

(Ref: :contentReference[oaicite:0]{index=0})

---

## 📊 Dataset Summary
- **Total Records:** 3,900 transactions  
- **Features:** 18 columns  
- **Data Includes:**
  - Customer demographics (Age, Gender, Location, Subscription Status)
  - Purchase details (Category, Amount, Season, Size, Color)
  - Behavioral metrics (Discount usage, Frequency, Ratings, Shipping type)

- **Data Quality:**
  - Missing values handled (Review Rating column)

(Ref: :contentReference[oaicite:1]{index=1})

---

## 🛠️ Tech Stack
- **Python** – Data cleaning, preprocessing, feature engineering  
- **SQL (PostgreSQL)** – Business analysis & querying  
- **Power BI** – Data visualization & dashboarding  
- **Pandas, NumPy** – Data manipulation  

---

## 🔄 Project Workflow

### 1️⃣ Data Preparation (Python)
- Cleaned and transformed raw data
- Handled missing values using median imputation
- Standardized column names (snake_case)
- Performed feature engineering:
  - Age group segmentation
  - Purchase frequency metrics
- Loaded cleaned data into PostgreSQL

---

### 2️⃣ Data Analysis (SQL)
Performed business-focused analysis including:

- Revenue analysis by gender
- High-spending customers using discounts
- Top-rated products
- Shipping type impact on purchase value
- Subscription vs non-subscription revenue
- Customer segmentation (New, Returning, Loyal)
- Repeat purchase behavior analysis
- Revenue contribution by age group

---

### 3️⃣ Dashboard (Power BI)
Developed an interactive dashboard to visualize:
- Revenue trends
- Customer segmentation
- Category-wise sales
- Subscription insights
- Age group performance

---

## 🔍 Key Insights

- **Male customers generated higher revenue** compared to female customers  
- **Discount users can still be high-value customers**  
- **Top-rated products drive consistent engagement**  
- **Express shipping users tend to spend slightly more**  
- **Majority of customers are in the "Loyal" segment**  
- **Young adults contribute the highest revenue share**  

---

## 💡 Business Recommendations

- 🎯 Promote subscription programs to increase retention  
- 🔁 Strengthen loyalty programs for repeat customers  
- 💸 Optimize discount strategies to balance revenue and margin  
- ⭐ Highlight top-rated products in marketing campaigns  
- 📦 Encourage express shipping for higher order value  
- 👥 Target high-performing age groups with personalized campaigns  

---

## 📈 Project Deliverables
- Python data cleaning scripts  
- SQL analysis queries  
- Power BI dashboard  
- Business insights & recommendations  

---

## 📂 Repository Structure
