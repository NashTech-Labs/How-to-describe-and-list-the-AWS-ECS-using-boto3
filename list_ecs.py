# MuZakkir Saifi
# import the boto3 which will use to interact  with the aws

import boto3
REGION = input("Enter the REGION Name")

clientForEcs = boto3.client("ecs", region_name=REGION)

pag = clientForEcs.get_paginator('list_clusters')

res_iterator = pag.paginate(
    PaginationConfig={
        'PageSize':80
})

for x in res_iterator:
    for y in x['clusterArns']:
        print(y)