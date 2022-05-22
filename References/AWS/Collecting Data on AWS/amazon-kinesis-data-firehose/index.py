import base64
import json

print('Loading function')


def handler(event, context):
    output = []

    for record in event['records']:
        print(record['recordId'])
        payload = json.loads(base64.b64decode(record['data']))

        # Do custom processing on the data here
        output_payload = ""
        for i in payload:
            output_payload = output_payload + str(payload[i])
            output_payload = output_payload + ','
        output_payload[:-1]
        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': base64.b64encode(output_payload.encode())
        }
        output.append(output_record)

    print('Successfully processed {} records.'.format(len(event['records'])))

    return { 'records': output }