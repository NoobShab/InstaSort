import pandas as pd

# Input | Output of the files
INPUT_CSV = "reelsFromAccounts.csv"
OUTPUT_CSV = "reelsArrangement.csv"

# Read the CSV file
df = pd.read_csv(INPUT_CSV)

# identify hashtag columns
hashtag_columns = [col for col in df.columns if col.startswith("hashtags/")]

rows = []

for _, row in df.iterrows():
    reel_id = row["id"]
    views = row["videoViewCount"]
    likes = row["likesCount"]
    comments = row["commentsCount"]
    timestamp = row["timestamp"]

    for col in hashtag_columns:
        hashtag = row[col]

        if pd.notna(hashtag) and hashtag != "":
            rows.append({
                "reel_id" : reel_id,
                "views" : views,
                "likes" : likes,
                "comments" : comments,
                "hashtag" : hashtag.lower(),
                "timestamp" : timestamp
            })

# Now create arranged dataframe
arranged_df = pd.DataFrame(rows)

# Save to CSV
arranged_df.to_csv(OUTPUT_CSV, index = False)

print(f"Normalization complete. Saved to {OUTPUT_CSV}")
            