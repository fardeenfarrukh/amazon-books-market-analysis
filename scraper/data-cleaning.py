import pandas as pd

df = pd.read_csv("data/raw/books_raw.csv")

print("Original dataset shape:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())

print("\nData types:")
print(df.dtypes)

print("\nMissing values:")
print(df.isnull().sum())

print("\nDuplicate records:", df.duplicated().sum())

print("\nPrice examples:")
print(df["Price (excl. tax)"].head().tolist())

print("\nAvailability examples:")
print(df["Availability"].head().tolist())

print("\nRating examples:")
print(df["BookRating"].unique())

print("\nDescription examples:")
print(df["BookDescription"].head().tolist())

df = df.drop_duplicates(subset=["ProductURL"])

for column in ["Price (excl. tax)", "Price (incl. tax)", "Tax"]:
    df[column] = pd.to_numeric(
        df[column].str.replace("£", "", regex=False)
    )

rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}
df["BookRating"] = df["BookRating"].map(rating_map)
df["StockQuantity"] = df["Availability"].str.extract(r"(\d+)").astype(int)
df["BookTitle"] = df["BookTitle"].str.strip()
df["BookDescription"] = df["BookDescription"].fillna("").str.strip()

df.to_csv("data/cleaned/books_cleaned.csv", index=False, encoding="utf-8-sig")

print("\nCleaned dataset shape:", df.shape)
print("\nCleaned data types:")
print(df.dtypes)
print("\nCleaned dataset saved successfully!")