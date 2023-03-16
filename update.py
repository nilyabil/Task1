from google.cloud import storage


project_id = "qwiklabs-gcp-04-46bcc0026893"
client = storage.Client(project_id)
bucket = client.get_bucket('qwiklabs-gcp-04-46bcc0026893')
blob = bucket.blob('demo.txt')

with blob.open("w") as f:
        f.write("Hello world")

with blob.open("r") as f:
        print(f.read())