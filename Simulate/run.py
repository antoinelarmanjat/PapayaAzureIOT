import json
import os
import random
import sys

# adding the shared libraries path, must be done before the libraries are imported
sys.path.append(os.path.abspath(os.path.join(os.path.dirname( __file__ ), "..", "Lib")))
# shared libraries
from repository import repository
from iothub import iothub

AVG_WINDSPEED = 10 # m/s
AVG_POWEROUTPUT = 800 #kW

devices = repository.list_devices()
for id, pk in devices:
    currWindSpeed = AVG_WINDSPEED + random.random() * 4 - 2
    currPowerOutput = AVG_POWEROUTPUT + random.random() * 200 - 100
    event = {"deviceId": id, "windSpeed": currWindSpeed, "powerOutput": currPowerOutput}
    iothub.emit(id, pk, json.dumps(event))
