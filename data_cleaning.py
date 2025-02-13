import pandas as pd

# Load the dataset
file_path = "insurance.csv"  
df = pd.read_csv(file_path)

# Step 1: View initial data info
print("Initial Data Info:")
print(df.info())

# Step 2: Check and Print Column Names
print("Available Columns:", df.columns)

# Step 3: Handle Missing Data
df.ffill(inplace=True)  # Forward fill missing values

# Step 4: Correct Filtering Step (Choose the Right Column)
df = df[df["smoker"] != "yes"]  # Example: Removing smokers

# Step 5: Aggregate Data (Sum of charges per region)
aggregated_df = df.groupby("region").agg({"charges": "sum"}).reset_index()

# Step 6: Save cleaned and transformed data
aggregated_df.to_csv("cleaned_insurance.csv", index=False)

print("Data cleaning and transformation completed successfully!")