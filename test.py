from azure.storage.blob import BlobServiceClient
import os

# Azure Blob Storage configuration
with open("connection_string", "r") as f:
    CONNECTION_STRING = f.read().strip()

# Initialize BlobServiceClient
blob_service_client = BlobServiceClient.from_connection_string(CONNECTION_STRING)

def upload_file_to_blob(file_path, blob_name, container_name):
    try:
        # Get the container client
        container_client = blob_service_client.get_container_client(container_name)
        
        # Upload the file
        with open(file_path, "rb") as data:
            container_client.upload_blob(name=blob_name, data=data, overwrite=True)
        
        print(f"File {blob_name} uploaded successfully.")
        return f"https://{blob_service_client.account_name}.blob.core.windows.net/{container_name}/{blob_name}"
    except Exception as e:
        print(f"Error uploading file: {e}")
        return None

def download_file_from_blob(blob_name, download_path, container_name):
    try:
        # Get the container client
        container_client = blob_service_client.get_container_client(container_name)
        
        # Get the blob client
        blob_client = container_client.get_blob_client(blob_name)
        
        # Download the blob
        with open(download_path, "wb") as download_file:
            download_file.write(blob_client.download_blob().readall())
        
        print(f"File {blob_name} downloaded successfully to {download_path}.")
    except Exception as e:
        print(f"Error downloading file: {e}")

if __name__ == '__main__':

    response = input("Enter 'upload' to upload a file, 'download' to download a file: ")

    CONTAINER_NAMES = ["gamevideos", "submissions"]

    chosen_container = input(f"Choose a container to upload to ({CONTAINER_NAMES}): ")

    if response == "upload":
        # Example usage
        file_path = input("Enter the path of the file to upload: ")
        blob_name = input("Enter the name of the blob: ")
        uploaded_url = upload_file_to_blob(file_path, blob_name, chosen_container)
        if uploaded_url:
            print(f"File available at: {uploaded_url}")
    else:
        # Example usage
        blob_name = input("Enter the name of the blob to download: ")
        download_path = input("Enter the path to download the file: ") + blob_name
        download_file_from_blob(blob_name, download_path, chosen_container)
