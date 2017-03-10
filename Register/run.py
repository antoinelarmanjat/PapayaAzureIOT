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

with open(os.environ["REQ"]) as req:
    details = json.loads(req.read())

# first register the device with the Azure IoT Hub
did, dpk = iothub.add_device(uuid.uuid4())
# then inform Papaya about the device
pid, ptk = papaya.register(did)
# extend the device details with Papaya & Azure ids
details["deviceId"] = did
details["papayaId"] = pid
details["papayaToken"] = ptk
# finally insert the full details in Azure Document DB
repository.insert(did, details)