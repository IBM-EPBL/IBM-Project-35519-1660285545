import ibm_boto3
from ibm_botocore.client import Config
COS_ENDPOINT = "https://s3.us-south.cloud-object-storage.appdomain.cloud"
COS_API_KEY_ID = "XeBH2fKlSob0m2Spu-SwWC9Y7bG4elRjQw15-Jfv9udj"
COS_INSTANCE_CRN = "crn:v1:bluemix:public:cloud-object-storage:global:a/6b67b7ff45694a1fb1eae3387c6aa956:0968c6d0-3e25-4add-8b8d-5ed52e2c0988::"
COS_STORAGE_CLASS = "us-south"
cos = ibm_boto3.client("s3", ibm_api_key_id=COS_API_KEY_ID, ibm_service_instance_id=COS_INSTANCE_CRN, config=Config(signature_version="oauth"), endpoint_url=COS_ENDPOINT)
cos.create_bucket(
    Bucket="aaag10",
    CreateBucketConfiguration={
        "LocationConstraint":COS_STORAGE_CLASS
    }
)