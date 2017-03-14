import datetime
import json
import os
import random
import sys

# adding the shared libraries path, must be done before the libraries are imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), "..", "Lib")))
# shared libraries
from iothub import iothub

AVG_WINDSPEED = 10 # m/s
AVG_POWEROUTPUT = 800 #kW

response, _code = iothub.list_devices()
devices = json.loads(response)
for device in devices:
    currWindSpeed = AVG_WINDSPEED + random.random() * 4 - 2
    currPowerOutput = AVG_POWEROUTPUT + random.random() * 200 - 100
    now = "%s" % datetime.datetime.now()
    event = {"deviceId": device["deviceId"], "windSpeed": currWindSpeed, "powerOutput": currPowerOutput, "eventDate": now}
    iothub.emit_message(id, json.dumps(event))
