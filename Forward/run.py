import os
import json


inputMessage = open(os.environ['inputMessage']).read()
event = json.loads(inputMessage)

print(json.dumps(event))