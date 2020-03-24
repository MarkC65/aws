import boto3

client = boto3.client('elbv2')

response = client.create_target_group( \
    Name='tg3', \
    Port=80, \
    Protocol='HTTP', \
    VpcId='vpc-04894779c98b13ed4' \
)

print(response)

