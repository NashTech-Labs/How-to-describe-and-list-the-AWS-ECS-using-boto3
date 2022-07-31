# import the boto3 which will use to interact  with the aws

import boto3
import json
AWS_REGION = input("Enter the AWS_REGION Name")

client = boto3.client("ecs", region_name=AWS_REGION)

paginator = client.get_paginator('list_clusters')

response_iterator = paginator.paginate(
    PaginationConfig={
        'PageSize':100
})

for page in response_iterator:
    for arn in page['clusterArns']:
        response = client.describe_clusters(clusters=[arn])
        print(json.dumps(response, indent=4))