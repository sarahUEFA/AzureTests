from azure.storage.blob import BlobServiceClient
from azure.storage.blob import generate_blob_sas, BlobSasPermissions
from datetime import datetime, timedelta
from azure.mgmt.storage import StorageManagementClient
from azure.identity import DefaultAzureCredential
import os 

# Set your SAS token, storage account name, and container name
BlobEndpoint="https://aedrawappprd.blob.core.windows.net/"
QueueEndpoint="https://aedrawappprd.queue.core.windows.net/"
FileEndpoint="https://aedrawappprd.file.core.windows.net/"
TableEndpoint="https://aedrawappprd.table.core.windows.net/"
sas_token="sv=2022-11-02&ss=bfqt&srt=sco&sp=rwlacupitfx&se=2025-07-15T18:26:55Z&st=2024-07-15T10:26:55Z&spr=https&sig=HXYvwVK2eW6FoIPkHP9SRZJRr0kn%2BvAq%2BJAYDCOf9sM%3D"

container_name = "test"
file_dir = os.path.join(os.getcwd(),"Checker Results")
file_path  = os.path.join(file_dir,"AE_vs_ASOLVO_UCL_24_25_2024-06-03_LT_COMPLETED-SELECTION_Check_0.json")
file_name = os.path.basename(file_path)

# Create a BlobServiceClient using the SAS token
blob_service_client = BlobServiceClient(account_url=f"{BlobEndpoint}", credential=sas_token)

# Upload the file to the blob
blob_client = blob_service_client.get_blob_client(container_name, file_name)

with open(file_path, "rb") as data:
    blob_client.upload_blob(data)
