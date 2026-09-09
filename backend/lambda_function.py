import boto3
import json

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('VisitorCounter')

def lambda_handler(event, context):
    response = table.update_item(
        Key={'id': 'counter'},
        UpdateExpression='SET #c = #c + :incr',
        ExpressionAttributeNames={'#c': 'count'},
        ExpressionAttributeValues={':incr': 1},
        ReturnValues='UPDATED_NEW'
    )

    return {
        'statusCode': 200,
        'headers': {
            'Access-Control-Allow-Origin': '*',
            'Content-Type': 'application/json'
        },
        'body': json.dumps({'count': int(response['Attributes']['count'])})
    }
