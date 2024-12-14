#import packages
from google.cloud import storage
import os


# Load GCP credentials from a configuration file
def load_config(config_file):
    config = {}
    with open(config_file, 'r') as f:
        for line in f:
            # Ignore comments and blank lines
            line = line.strip()
            if line and not line.startswith("#"):
                key, value = line.split("=", 1)
                config[key.strip()] = value.strip()
    return config



# Create bucket
def create_gcp_bucket(bucket_name, config_file, storage_class='STANDARD', location='us-central1'): 

    # Load configuration
    config = load_config(config_file)

    # Set the environment variable for Google Cloud authentication
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = config["GCP_CREDENTIALS_PATH"]

    # Initialize a client
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)
    bucket.storage_class = storage_class
   
    bucket = storage_client.create_bucket(bucket, location=location) 
    # for dual-location buckets add data_locations=[region_1, region_2]
    
    return f'Bucket {bucket.name} successfully created.'


# if __name__ == "__main__":
#     # Configuration file path
#     CONFIG_FILE = "config.conf"

#     # GCP bucket details
#     BUCKET_NAME = "bucket_01"
#     SOURCE_FILE_PATH = "sample_data.csv"  # Replace with your CSV file path
#     DESTINATION_BLOB_NAME = "uploads/sample_data.csv"  # Desired path in the bucket

# Call the function
print(create_gcp_bucket('test_demo_storage_bucket', 'config.conf', 'STANDARD', 'us-central1'))
