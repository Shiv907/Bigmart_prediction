import mlflow.sagemaker as mfs

experiment_id = '4'
run_id = '89a357e2b0aa4722b7fefeed526d3d87'
region = 'ap-south-1'
aws_id = '893148189164'
arn = 'arn:aws:iam::893148189164:role/aws-mlflow-model'
app_name = 'model-app2'
model_uri = f"artifacts/{experiment_id}/{run_id}/artifacts/RFmodel4"
tag_id = '2.3.2'

image_url = f"{aws_id}.dkr.ecr.{region}.amazonaws.com/mlflow-pyfunc:{tag_id}"

# Delete the existing endpoint if it exists
endpoint_name = app_name + "-endpoint"
try:
    mfs.delete_endpoint(endpoint_name=endpoint_name, region_name=region)
    print("Existing endpoint deleted successfully.")
except:
    print("No existing endpoint found.")

# Deploy the new model
mfs._deploy(app_name=app_name, model_uri=model_uri, image_url=image_url, region_name=region, mode="replace",
           execution_role_arn=arn, timeout_seconds=3600)
