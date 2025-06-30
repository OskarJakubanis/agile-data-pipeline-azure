from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

# Dane logowania (zastąp swoimi)
AZURE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=...;AccountKey=...;EndpointSuffix=core.windows.net"
CONTAINER_NAME = "ecommerce-data"
BLOB_NAME = "validated/validated_orders.csv"
LOCAL_FILE = "validated_orders.csv"

# Połączenie z kontenerem
blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=BLOB_NAME)

# Wysłanie pliku do chmury
with open(LOCAL_FILE, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)

print(f"✅ Plik '{LOCAL_FILE}' został przesłany do Azure Blob Storage jako '{BLOB_NAME}'.")
