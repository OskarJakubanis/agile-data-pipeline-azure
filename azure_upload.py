# scripts/azure_upload.py

from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import os

# Dane do konfiguracji (w rzeczywistości użyj .env / Azure Key Vault dla bezpieczeństwa)
AZURE_CONNECTION_STRING = "DefaultEndpointsProtocol=https;AccountName=your_account;AccountKey=your_key;EndpointSuffix=core.windows.net"
CONTAINER_NAME = "ecommercedata"

# Folder lokalny z plikami CSV
LOCAL_DATA_FOLDER = "data"

def upload_files_to_blob():
    blob_service_client = BlobServiceClient.from_connection_string(AZURE_CONNECTION_STRING)
    try:
        container_client = blob_service_client.get_container_client(CONTAINER_NAME)
        container_client.create_container()
        print(f"Utworzono kontener: {CONTAINER_NAME}")
    except Exception as e:
        print(f"Korzystam z istniejącego kontenera: {CONTAINER_NAME}")

    for filename in os.listdir(LOCAL_DATA_FOLDER):
        if filename.endswith(".csv"):
            blob_client = blob_service_client.get_blob_client(container=CONTAINER_NAME, blob=filename)
            local_file_path = os.path.join(LOCAL_DATA_FOLDER, filename)
            with open(local_file_path, "rb") as data:
                blob_client.upload_blob(data, overwrite=True)
                print(f"✔️ Załadowano: {filename}")

if __name__ == "__main__":
    upload_files_to_blob()
