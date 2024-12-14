#import packages
from google.cloud import storage
import os


# set key credentials file path
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = 'config/datahub-dev-443818-0d0aef867dc4.json'

# Create bucket
def create_gcp_bucket(bucket_name, storage_class='STANDARD', location='us-central1'): 

    # Initialize a client
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = storage_class
   
    bucket = storage_client.create_bucket(bucket, location=location) 
    # for dual-location buckets add data_locations=[region_1, region_2]
    
    return f'Bucket {bucket.name} successfully created.'


# Call the function
print(create_gcp_bucket('datahub_demo_bucket_006', 'STANDARD', 'us-central1'))
