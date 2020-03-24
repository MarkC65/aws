'''
	DOCSTRING: This function uses paginator to retrieve a list of Target Groups one at a time, and delete the Target Group with a Name that matches 'tg3'.  The Target Group names and ARNs are printed as they are retrieved

'''

import boto3

client = boto3.client('elbv2')
paginator = client.get_paginator('describe_target_groups')

response_iterator = paginator.paginate(\
    PaginationConfig={\
        'MaxItems': 10,\
        'PageSize': 1,\
        'StartingToken': ''\
    })

for ri in response_iterator:
	tg=ri['TargetGroups']
	for tg_item in tg:
		print(tg_item['TargetGroupName']+'\n'+tg_item['TargetGroupArn'])
		if tg_item['TargetGroupName']=='tg3':
			print('Deleting {0}'.format(tg_item['TargetGroupName']))
			client.delete_target_group(TargetGroupArn=tg_item['TargetGroupArn'])
			print('Done')
	print ('===================\n')
