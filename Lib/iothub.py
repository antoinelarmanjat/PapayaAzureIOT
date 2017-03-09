class IoTHub:
    def __init__(self):
        pass

    def add(self, deviceId):
        pass

    def emit(self, deviceId, primaryKey, message):
        print "Emitting on %s" % message

iothub = IoTHub()