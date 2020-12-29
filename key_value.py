import boto3
from trp import Document


# Document
s3BucketName = "textract-acord-poc"
documentName = "Capture.PNG"
# Amazon Textract client
textract = boto3.client('textract')
# Call Amazon Textract
response = textract.analyze_document(
    Document={
        'S3Object': {
            'Bucket': s3BucketName,
            'Name': documentName
        }
    },
    FeatureTypes=["FORMS"])
import pdb
pdb.set_trace()
#print(response)
doc = Document(response)
f = open("key_value_output.txt", "w")
for page in doc.pages:
    # Print fields
    print("Fields:")
    for field in page.form.fields:
        print(field.key, ": ", field.value)
        f.write(str(field.key) + ": " + str(field.value) + "\n")
    # Get field by key
    print("\nGet Field by Key:")
    key = "Phone Number:"
    field = page.form.getFieldByKey(key)
    if(field):
        print(field.key, ": ", field.value)
        f.write(str(field.key) + ": " + str(field.value) + "\n")
    # Search fields by key
    print("\nSearch Fields:")
    key = "address"
    fields = page.form.searchFieldsByKey(key)
    for field in fields:
        print(field.key, ": ", field.value)
        f.write(str(field.key) + ": " + str(field.value) + "\n")