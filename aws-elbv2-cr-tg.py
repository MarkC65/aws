import boto3

client = boto3.client('elbv2')

response = client.create_target_group( \
    Name='tg3', \
    Port=80, \
    Protocol='HTTP', \
    VpcId='vpc-id' \
)

print(response)

