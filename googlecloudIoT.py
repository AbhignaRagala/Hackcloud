#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Import the necessary Google Cloud IoT and authentication libraries
from google.cloud import iot_v1
from google.oauth2 import service_account

# Authenticate to Google Cloud IoT using service account credentials
# Replace 'service_account.json' with the path to your service account key file
credentials = service_account.Credentials.from_service_account_file(
    'service_account.json',
    scopes=['https://www.googleapis.com/auth/cloud-platform']
)
client = iot_v1.DeviceManagerClient(credentials=credentials)

# Define IoT Core registry and device details
# Replace these values with your specific project, location, registry, and device IDs
project_id = 'clodhackhackathon'       # Your Google Cloud project ID
location = 'us-central1'             # The Google Cloud region
registry_id = 'your-registry-id'     # The name of your IoT Core registry
device_id = 'device-id'             # The name of your IoT device

# Create the device
# 'parent' is a formatted path specifying the project, location, and registry
parent = client.registry_path(project_id, location, registry_id)

# Define the device template with the device ID
device_template = {
    "id": device_id
}

# Create the device by sending a request with the parent and device template
device = client.create_device(request={"parent": parent, "device": device_template})


# to store the collected data from iot device in google cloud storage

# In[ ]:


from google.cloud import storage

def write_to_gcs(data, bucket_name, file_name):
    client = storage.Client()
    bucket = client.get_bucket(bucket_name)
    blob = bucket.blob(file_name)
    blob.upload_from_string(data)

# Usage:
# write_to_gcs(preprocessed_data, 'your-bucket-name', 'preprocessed_eeg_data.json')

