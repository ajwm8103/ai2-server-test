from azure.storage.blob import BlobServiceClient
import os

# Azure Blob Storage configuration
with open("connection_string", "r") as f:
    CONNECTION_STRING = f.read().strip()
CONTAINER_NAME = "gamevideos"

# Initialize BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)

def upload_file_to_blob(file_path, blob_name):
    try:
        # Get the container client
        container_client = blob_service_client.get_container_client(CONTAINER_NAME)
        
        # Upload the file
        with open(file_path, "rb") as data:
            container_client.upload_blob(name=blob_name, data=data, overwrite=True)
        
        print(f"File {blob_name} uploaded successfully.")
        return f"https://{blob_service_client.account_name}.blob.core.windows.net/{CONTAINER_NAME}/{blob_name}"
    except Exception as e:
        print(f"Error uploading file: {e}")
        return None

# Example usage
file_path = "clip.mp4"
blob_name = "example_video.mp4"
uploaded_url = upload_file_to_blob(file_path, blob_name)
if uploaded_url:
    print(f"File available at: {uploaded_url}")
