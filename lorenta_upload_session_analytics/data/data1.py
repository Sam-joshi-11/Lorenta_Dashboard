import pandas as pd
merged = pd.read_csv("merged_data.csv")

analytics = (
    merged.groupby("session_id")
    .agg(
        user_email=("user_email", "first"),
        status=("status", "first"),
        total_amount=("total_amount", "first"),
        total_sheets=("total_sheets", "first"),

        monochrome_sheets=(
            "number_of_pages",
            lambda x: x[
                merged.loc[x.index, "printing_mode"].str.lower() == "monochromatic"
            ].sum()
        ),

        color_sheets=(
            "number_of_pages",
            lambda x: x[
                merged.loc[x.index, "printing_mode"].str.lower() == "color"
            ].sum()
        ),

        monochrome_revenue=(
            "price",
            lambda x: x[
                merged.loc[x.index, "printing_mode"].str.lower() == "monochromatic"
            ].sum()
        ),

        color_revenue=(
            "price",
            lambda x: x[
                merged.loc[x.index, "printing_mode"].str.lower() == "color"
            ].sum()
        ),

        created_at=("created_at_y", "first")
    )
    .reset_index()
)

print("Original Revenue :", analytics["total_amount"].sum())
print("Split Revenue    :", analytics["monochrome_revenue"].sum() + analytics["color_revenue"].sum())

print("Original Sheets  :", analytics["total_sheets"].sum())
print("Split Sheets     :", analytics["monochrome_sheets"].sum() + analytics["color_sheets"].sum())