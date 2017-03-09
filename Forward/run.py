import os, sys
import json

# adding the shared libraries path, must be done before the libraries are imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), "..", "Lib")))
# shared libraries
from repository import repository
from papaya import papaya

with open(os.environ["inputMessage"]) as msg:
    event = json.loads(msg.read())

papayaId, papayaToken = repository.resolve(event["deviceId"])

payload = { "Urgent": False, "Unit": "washstop", "Amount": "%.1f" % event["totalpoweroutput"] }

response = papaya.update(papayaId, papayaToken, payload)

print response.text
