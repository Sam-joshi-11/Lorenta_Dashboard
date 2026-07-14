import pandas as pd
import pandas as pd

# Read CSV files
files = pd.read_csv("upload_files.csv")
sessions = pd.read_csv("upload_sessions (1).csv")

# Remove rows containing any NULL values
files = files.dropna()
sessions = sessions.dropna()

# Remove unwanted statuses
sessions = sessions[
    ~sessions["status"].str.strip().str.lower().isin(["priced", "created"])
]

# Merge the tables
merged = pd.merge(
    files,
    sessions,
    left_on="session_id",
    right_on="id",
    how="inner"
)

# Save the merged data
merged.to_csv("merged_data.csv", index=False)

print(merged.head())
print(merged.shape)