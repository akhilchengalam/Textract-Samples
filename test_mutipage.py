import random
import boto3
from trp import Document


bucket = "textract-acord-poc"
filename = "Multipage_test.pdf"

client = boto3.client('textract')
response = client.start_document_analysis(
    DocumentLocation={'S3Object': {'Bucket': bucket, 'Name': filename}},
    FeatureTypes=["TABLES", "FORMS"])
import pdb
pdb.set_trace()
print(response)
res = client.get_document_analysis(JobId=response["JobId"])
doc = Document(res)
print(doc)