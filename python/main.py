import json

def lambda_handler(event, context):
    decodedEvent = json.loads(event['body'])
    words = decodedEvent['input_text']
    replaceList = ['Oracle', 'Google', 'Microsoft', 'Amazon', 'Deloitte']
    for item in replaceList:
        if item in words:
            new_item = item + '\u00a9'
            words = words.replace(item,new_item)
    # return words
    
    return {
        'statusCode': 200,
        'body': words
    }
