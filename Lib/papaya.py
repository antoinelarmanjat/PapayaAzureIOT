import json

import requests


class Papaya:
    def __init__(self):
        pass

    def register(self, deviceId, devicePublicKey, manufacturerId, payerId, payeeId, payeeToken):
        headers = { "Authorization": payeeToken, "Content-Type": "application/json", "Cache-Control": "no-cache" }
        payload = { "ExternalId": deviceId, "PublicKey": devicePublicKey,
                    "ManufacturerId": manufacturerId, "DeviceType": "WindTurbine"}
        r = requests.post("https://api.papayagogo.com/%s/%s/devices" % (payeeId, payerId),
            headers=headers, data=json.dumps(payload))
        jr = json.loads(r.text)
        return jr["_id"], jr["Token"]

    def update(self, id, token, payload):
        headers = { "Authorization": token, "Content-Type": "application/json", "Cache-Control": "no-cache" }
        return requests.post("https://api.papayagogo.com/%s/event" % id, headers=headers, data=json.dumps(payload))

papaya = Papaya()
