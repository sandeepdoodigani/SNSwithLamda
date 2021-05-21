import json
import boto3
sns = boto3.client('sns')
def lambda_handler(event, context):
    # TODO implement
    response = sns.publish(TopicArn='arn:aws:sns:ap-south-1:769148881933:smartinternz',Message='Hello World',Subject="Testing",)
    print(response)
    return {
        'statusCode': 200,
        'body': json.dumps(response)
    }
