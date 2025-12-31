import json
import boto3
import uuid

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('Subscribers')

polly = boto3.client('polly')
ses = boto3.client('ses')
s3 = boto3.client('s3')

BUCKET_NAME = "YOUR_S3_BUCKET_NAME"
FROM_EMAIL = "YOUR_VERIFIED_SES_EMAIL"

VOICE_MAP = {
    "en": "Joanna",
    "hi": "Aditi",
    "fr": "Celine",
    "de": "Vicki",
    "es": "Lucia"
}

def lambda_handler(event, context):
    body = json.loads(event['body'])

    name = body.get('name', 'Subscriber')
    email = body['email']
    language = body.get('language', 'en')

    token = str(uuid.uuid4())

    table.put_item(
        Item={
            "email": email,
            "name": name,
            "language": language,
            "token": token
        }
    )

    text = f"Hello {name}, welcome to our voice newsletter."

    response = polly.synthesize_speech(
        Text=text,
        VoiceId=VOICE_MAP.get(language, "Joanna"),
        OutputFormat='mp3'
    )

    audio_key = f"welcome/{email}.mp3"
    s3.put_object(
        Bucket=BUCKET_NAME,
        Key=audio_key,
        Body=response['AudioStream'].read()
    )

    audio_url = s3.generate_presigned_url(
        ClientMethod='get_object',
        Params={'Bucket': BUCKET_NAME, 'Key': audio_key},
        ExpiresIn=604800
    )

    ses.send_email(
        Source=FROM_EMAIL,
        Destination={'ToAddresses': [email]},
        Message={
            'Subject': {'Data': 'Welcome to Voice Newsletter'},
            'Body': {
                'Html': {
                    'Data': f'<p>Click below to listen:</p><a href="{audio_url}">Play Audio</a>'
                }
            }
        }
    )

    return {
        "statusCode": 200,
        "headers": {"Access-Control-Allow-Origin": "*"},
        "body": "Subscription successful"
    }
