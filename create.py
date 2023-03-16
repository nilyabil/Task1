
from google.cloud import storage

project_id = "qwiklabs-gcp-02-15813f0080fd"
bucket_name = "qwiklabs-gcp-02-15813f0080fda"
storage_client = storage.Client(project_id)
bucket = storage_client.create_bucket(bucket_name)

print(f"Bucket {bucket.name} created.")