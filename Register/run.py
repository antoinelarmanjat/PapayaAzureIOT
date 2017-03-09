import json
import os
import sys
import uuid

# adding the shared libraries path, must be done before the libraries are imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), "..", "Lib")))
# shared libraries
from iothub import iothub
from papaya import papaya
from repository import repository

print os.environ["REQ_QUERY_CODE"]

with open(os.environ["REQ"]) as req:
    details = json.loads(req.read())

did, dpk = iothub.add(uuid.uuid4())
pid, ptk = papaya.register(did)

details["deviceId"] = did
details["devicePrimaryKey"] = dpk
details["papayaId"] = pid
details["papayaToken"] = ptk

repository.insert(did, details)