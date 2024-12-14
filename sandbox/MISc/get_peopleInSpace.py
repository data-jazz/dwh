import requests
import json
import configparser
import csv
from google.cloud import storage
import os


api_response = requests.get("http://api.open-notify.org/astros.json")
# print(api_response.content)


# create a json object from the response content
response_json = json.loads(api_response.content)
all_passes = []
for people in response_json['people']:
    current_pass = []
# #store the lat/log from the request
#     current_pass.append(lat)
#     current_pass.append(lon)
# store the duration and risetime of the pass
    current_pass.append(people['name'])
    current_pass.append(people['craft'])
    all_passes.append(current_pass)
export_file = "export_file01.csv"
with open(export_file, 'w') as fp:
    csvw = csv.writer(fp, delimiter='|')
    csvw.writerows(all_passes)
fp.close()


# Extract GCP configurations
parser = configparser.ConfigParser()
parser.read("config/pipeline.conf")

bucket_name = parser.get("gcp_creds","bucket_name")
service_account_key = parser.get("gcp_creds","service_account_key")

# Set the environment variable for GCP authentication
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = service_account_key


# define function that uploads a file from the bucket
def upload_cs_file(bucket_name, source_file_name, destination_file_name): 
    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(destination_file_name)
    blob.upload_from_filename(source_file_name)

    return True

upload_cs_file(bucket_name, export_file, export_file)


