from google.cloud import storage

# Set the credentials and the name of the bucket you want to upload the file to.
# storage_client = storage.Client.from_service_account_json('D:\python\Google\key.json')
bucket_name = 'qwiklabs-gcp-04-23523374b46f'
project_id='qwiklabs-gcp-04-23523374b46f'
storage_client = storage.Client(project_id)

# Set the path to the local file you want to upload.
local_file_path = 'D:\python\Google\demo.txt'

# Set the name of the file you want to upload to GCS.
destination_blob_name = 'demo1.txt'

# Get the bucket object you want to upload to.
bucket = storage_client.bucket(bucket_name)

# Upload the file to GCS.
blob = bucket.blob(destination_blob_name)
blob.upload_from_filename(local_file_path)

print(f'File {local_file_path} uploaded to gs://{bucket_name}/{destination_blob_name}.')
