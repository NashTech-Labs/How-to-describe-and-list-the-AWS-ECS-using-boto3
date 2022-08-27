# import the boto3 which will use to interact  with the aws

import boto3
import json
REGION = input("Enter the REGION Name")

client_for_ECS = boto3.client("ecs", region_name=REGION)

pag = client_for_ECS.get_paginator('list_clusters')

res_iterator = pag.paginate(
    PaginationConfig={
        'PageSize':80
})

for x in res_iterator:
    for arn in x['clusterArns']:
        result = client_for_ECS.describe_clusters(clusters=[arn])
        print(json.dumps(result, indent=4))