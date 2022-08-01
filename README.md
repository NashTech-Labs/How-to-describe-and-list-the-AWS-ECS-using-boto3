## How to describe and list the AWS ECS using boto3.

#### Amazon Elastic Container Service (Amazon ECS) is a highly scalable and fast container management service. You can use it to run, stop, and manage containers on a cluster. With Amazon ECS, your containers are defined in a task definition that you use to run an individual task or task within a service. In this context, a service is a configuration that you can use to run and maintain a specified number of tasks simultaneously in a cluster. You can run your tasks and services on a serverless infrastructure that's managed by AWS Fargate. Alternatively, for more control over your infrastructure, you can run your tasks and services on a cluster of Amazon EC2 instances that you manage. You can follow this [link](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) to know more.

-------------

**Files:** 
```
      describe_ecs.py
      list_ecs.py
```

## Apply the script

1. First configure the aws credentials using aws-cli.

        aws configure

2. Now, from the current directory run the following command to describe and list the ECS.

        python3  describe_ecs.py
        python3 list_ecs.py

