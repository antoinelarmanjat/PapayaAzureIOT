import json
import requests

class Papaya:
    def __init__(self):
        pass

    def register(self, deviceId):
        pass

    def update(self, id, token, payload):
        headers = { "Authorization": token, "Content-Type": "application/json", "Cache-Control": "no-cache" }
        return requests.post("https://www.papayagogo.com/%s/event" % id, headers=headers, data=json.dumps(payload))

papaya = Papaya()