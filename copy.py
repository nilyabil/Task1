from google.cloud import storage


project_id='qwiklabs-gcp-04-23523374b46f'
storage_client = storage.Client(project_id)


# Source and destination bucket names
src_bucket_name = 'qwiklabs-gcp-04-23523374b46f'
src_blob_name = 'demo.txt'
dest_bucket_name = 'qwiklabs-gcp-04-23523374b46fa'
dest_blob_name = 'demo.txt'

# Get the source bucket and blob
src_bucket = storage_client.get_bucket(src_bucket_name)
src_blob = src_bucket.blob(src_blob_name)

# Create the destination bucket if it doesn't exist
dest_bucket = storage_client.bucket(dest_bucket_name)
if not dest_bucket.exists():
    dest_bucket.create()

# Copy the blob to the destination bucket
dest_blob = src_bucket.copy_blob(
    blob=src_blob, destination_bucket=dest_bucket, new_name=dest_blob_name
)

print(f'File {src_blob_name} copied to {dest_blob_name}.')
