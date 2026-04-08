import pandas as pd

# Load the three CSV files
df1 = pd.read_csv("data/daily_sales_data_0.csv")
df2 = pd.read_csv("data/daily_sales_data_1.csv")
df3 = pd.read_csv("data/daily_sales_data_2.csv")

# Combine them into one dataframe
df = pd.concat([df1, df2, df3], ignore_index=True)

# Standardise text just in case
df["product"] = df["product"].str.strip().str.lower()

# Keep only Pink Morsels
df = df[df["product"] == "pink morsel"]

# Create sales column
df["sales"] = df["quantity"] * df["price"]

# Keep only the required columns
df = df[["sales", "date", "region"]]

# Rename columns to match the task exactly
df.columns = ["Sales", "Date", "Region"]

# Save the final processed file
df.to_csv("processed_data.csv", index=False)

print("Done - processed_data.csv has been created")