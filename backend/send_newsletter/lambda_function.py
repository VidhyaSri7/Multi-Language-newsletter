import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Subscribers')
ses = boto3.client('ses')

FROM_EMAIL = "YOUR_VERIFIED_SES_EMAIL"

def lambda_handler(event, context):
    body = json.loads(event['body'])
    subject = body['subject']
    message = body['message']

    subscribers = table.scan()['Items']

    for user in subscribers:
        ses.send_email(
            Source=FROM_EMAIL,
            Destination={'ToAddresses': [user['email']]},
            Message={
                'Subject': {'Data': subject},
                'Body': {'Text': {'Data': message}}
            }
        )

    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": "Newsletter sent successfully"
    }
