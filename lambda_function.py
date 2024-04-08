import boto3


def lambda_handler(event, context):
    # event['context']['sub']
    # event['context']['http-method'] == 'GET'
    result = dict()
    result['status'] = 200
    result['message'] = 'Hello world'
    return result

    # if you choise Proxy Integration,
    # return {
    #     'statusCode': 200,
    #     'body': json.dumps(result),
    #     'headers': {
    #       'Access-Control-Allow-Origin': '*',
    #     }
    # }
