import pandas as pd
from sqlalchemy import create_engine

# Load dataset
df = pd.read_csv("customer_shopping_behavior.csv")

# Handle missing values
df["Review Rating"] = df.groupby("Category")["Review Rating"].transform(
    lambda x: x.fillna(x.median())
)

# Standardize column names
df.columns = df.columns.str.lower().str.replace(" ", "_")
df = df.rename(columns={"purchase_amount_(usd)": "purchase_amount"})

# Create age group column
labels = ["Young Adult", "Adult", "Middle-aged", "Senior"]
df["age_group"] = pd.qcut(df["age"], q=4, labels=labels)

# Create purchase frequency days column
frequency_mapping = {
    "Fortnightly": 14,
    "Weekly": 7,
    "Monthly": 30,
    "Quarterly": 90,
    "Bi-Weekly": 14,
    "Annually": 365,
    "Every 3 Months": 90
}
df["purchase_frequency_days"] = df["frequency_of_purchases"].map(frequency_mapping)

# Drop redundant column
if (df["discount_applied"] == df["promo_code_used"]).all():
    df = df.drop("promo_code_used", axis=1)

# PostgreSQL connection
username = "postgres"
password = "your_password"
host = "localhost"
port = "5432"
database = "customer_behavior"

engine = create_engine(
    f"postgresql+psycopg2://{username}:{password}@{host}:{port}/{database}"
)

# Load data into PostgreSQL
df.to_sql("customer", engine, if_exists="replace", index=False)

print("Data successfully loaded into PostgreSQL.")
