import pandas as pd

# Wczytanie danych z Azure Blob Storage lub lokalnie
df = pd.read_csv("orders.csv")

# Inicjalizacja zbiorów
valid_rows = []
invalid_rows = []
error_log = []

# Sprawdzanie każdego wiersza
for idx, row in df.iterrows():
    errors = []

    if pd.isnull(row['order_id']):
        errors.append("Missing order_id")
    if pd.isnull(row['customer_id']):
        errors.append("Missing customer_id")
    if pd.isnull(row['product_id']):
        errors.append("Missing product_id")
    if pd.isnull(row['order_date']):
        errors.append("Missing order_date")
    if row.get('quantity', 1) <= 0:
        errors.append("Invalid quantity")

    if errors:
        invalid_rows.append(row)
        error_log.append({
            "row_index": idx,
            "errors": ", ".join(errors),
            "data": row.to_dict()
        })
    else:
        valid_rows.append(row)

# Zapisanie poprawnych i błędnych danych
pd.DataFrame(valid_rows).to_csv("validated_orders.csv", index=False)
pd.DataFrame(invalid_rows).to_csv("rejected_orders.csv", index=False)
pd.DataFrame(error_log).to_json("error_report.json", orient="records", indent=2)
