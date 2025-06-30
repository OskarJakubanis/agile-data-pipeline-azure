import pandas as pd
from io import StringIO
from azure.storage.blob import BlobServiceClient

# Ustawienia połączenia
connect_str = "your_connection_string"
container_name = "data-pipeline"
input_blob_name = "orders.csv"
output_blob_name = "orders_cleaned.csv"

# Inicjalizacja klienta
blob_service_client = BlobServiceClient.from_connection_string(connect_str)
container_client = blob_service_client.get_container_client(container_name)

# Pobierz dane wejściowe z chmury
blob_client = container_client.get_blob_client(input_blob_name)
blob_data = blob_client.download_blob().readall()
orders = pd.read_csv(StringIO(blob_data.decode()))

# 🔧 Przetwarzanie danych
orders.dropna(subset=["order_id", "customer_id"], inplace=True)
orders["order_date"] = pd.to_datetime(orders["order_date"])
orders["total_value"] = orders["quantity"] * orders["unit_price"]

# Zapisz przetworzone dane do pamięci
output = StringIO()
orders.to_csv(output, index=False)
output_data = output.getvalue().encode()

# Prześlij przetworzone dane z powrotem do chmury
output_blob_client = container_client.get_blob_client(output_blob_name)
output_blob_client.upload_blob(output_data, overwrite=True)

print("✅ Orders cleaned and saved to Azure Blob Storage.")
