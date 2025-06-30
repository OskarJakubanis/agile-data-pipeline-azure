import pandas as pd

# Wczytaj oczyszczony plik
df = pd.read_csv("orders_cleaned.csv")

# Wczytaj surowy plik (przed czyszczeniem)
raw_df = pd.read_csv("orders_raw.csv")

# Znajdź rzędy, które miały braki w danych (NaN) w surowym pliku
rejected_rows = raw_df[raw_df.isnull().any(axis=1)].copy()

# Zbuduj raport błędów
error_log = []

for idx, row in rejected_rows.iterrows():
    for col in row.index:
        if pd.isnull(row[col]):
            error_log.append({
                "row_id": idx,
                "column_name": col,
                "error_type": "Missing value",
                "value": None
            })

# Konwertuj do DataFrame
error_df = pd.DataFrame(error_log)

# Zapisz do CSV
error_df.to_csv("rejected_rows.csv", index=False)

print("✅ Report of rejected rows saved as 'rejected_rows.csv'")
