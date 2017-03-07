import os,sys
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), "..", "env/Lib/site-packages")))

import pydocumentdb.documents as documents
import pydocumentdb.document_client as document_client
import requests


inputMessage = open(os.environ["inputMessage"]).read()
event = json.loads(inputMessage)

docDBHost = os.environ["docDBHost"]
docDBKey  = os.environ["docDBKey"]

client = document_client.DocumentClient(
    docDBHost, {"masterKey": docDBKey})

docs = list(client.QueryDocuments("dbs/devices/colls/deviceInfo", 
    "SELECT c.papayaId, c.papayaToken FROM c WHERE c.deviceId = '" + event["deviceid"] + "'"))

if len(docs) > 0:
    for doc in docs:
        h = {
            "Authorization": doc["papayaToken"], 
            "Content-Type": "application/json",
            "Cache-Control": "no-cache"
        }
        p = {
            "Urgent": False,
            "Unit": "washstop",
            "Amount": "%.1f" % event["totalpoweroutput"]
        }
        r = requests.post("https://www.papayagogo.com/%s/event" % doc["papayaId"], 
            headers=h, data=json.dumps(p))
        print r.text
