from google.cloud import storage


project_id = "qwiklabs-gcp-04-23523374b46f"
client = storage.Client(project=project_id)
bucket = client.get_bucket('qwiklabs-gcp-04-23523374b46f')
blob = bucket.blob('demo.txt')
contents = blob.download_as_string()
print(contents)
