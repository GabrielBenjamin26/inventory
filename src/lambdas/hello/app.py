import json
import requests
import bcrypt
import sys

def handler(event, context):
    name = b'anonymous'
    hashed = bcrypt.hashpw(name, bcrypt.gensalt())
    body = {
        "message": "{}, requests {}, bcrypt {} installed. hash generated: {}".
            format(sys.version, requests.__version__, bcrypt.__version__, hashed),
        "input": event
    }
    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }
    return response