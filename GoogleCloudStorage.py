#!/usr/bin/env python
# coding: utf-8

# In[1]:


import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/Users/abhignaragala/Downloads/hackcloud-399806-8b35517c9f77.json'


# In[2]:


from google.cloud import storage

# Initialize a client
client = storage.Client()


# In[3]:


from google.cloud import storage

# Initialize a client
client = storage.Client()

# Define your Google Cloud Storage bucket and object name
bucket_name = 'hackcloud'
object_name = 'my-object.txt'

# Upload the EEG data file to Google Cloud Storage
bucket = client.bucket(bucket_name)
blob = bucket.blob(object_name)
blob.upload_from_filename('/Users/abhignaragala/Downloads/Seizures_information.xlsx')


# In[4]:


from google.cloud import storage
import datetime

# Initialize the client
client = storage.Client()

# Specify your bucket and blob name
bucket_name = 'hackcloud'
blob_name = 'my-object.txt'

# Get the bucket and blob
bucket = client.get_bucket(bucket_name)
blob = bucket.blob(blob_name)

# Set the retention policy
your_retention_time = datetime.datetime(2023, 9, 27)
blob.retention_period = your_retention_time

# Update the blob's retention policy
blob.patch()


# In[ ]:




