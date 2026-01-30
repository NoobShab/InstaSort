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

# check for the invalid values
def clean_data(rows):
    cleaned = []

    for row in rows:
        views = int(row["views"])
        likes = int(row["likes"])

        if views == 0:
            continue #skip the reel
        if likes == -1:
            continue
            
        cleaned.append(row)

    return cleaned 

# Now create arranged dataframe
arranged_df = pd.DataFrame(clean_data(rows))

# Save to CSV
arranged_df.to_csv(OUTPUT_CSV, index = False)

print(f"Normalization complete. Saved to {OUTPUT_CSV}")
            