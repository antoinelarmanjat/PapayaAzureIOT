# adding the virtual env path, must be done before the libraries are imported
import envsetup

import os

import pydocumentdb.documents as documents
import pydocumentdb.document_client as document_client

class Repository:
    DB_NAME = "devices"
    COLL_NAME = "deviceInfo"
    COLLECTION = "dbs/%s/colls/%s" % (DB_NAME, COLL_NAME)

    def __init__(self, host, token):
        self.client = document_client.DocumentClient(host, {"masterKey": token})

    def _ensure_db_exists(self):
        # TODO ME hack as we haven't automated the db/coll construction through ARM
        if len(list(self.client.ReadDatabases())) == 0:
            self.client.CreateDatabase({"id": self.DB_NAME})
            props = {
                "id": self.COLL_NAME,
                "indexingPolicy": {
                    "indexingMode": "consistent"
                },
                "partitionKey": {
                    "paths": ["/deviceId"],
                    "kind": documents.PartitionKind.Hash
                }
            }
            self.client.CreateCollection("dbs/%s" % self.DB_NAME, props)

    def resolve(self, deviceId):
        self._ensure_db_exists()
        # TODO ME fix the potential SQL-I issue with the deviceId
        docs = list(self.client.QueryDocuments(self.COLLECTION,
            "SELECT c.papayaId, c.papayaToken FROM c WHERE c.deviceId = '%s'" % deviceId))
        if len(docs) > 0:
            return docs[0]["papayaId"], docs[0]["papayaToken"]
        else:
            raise KeyError("Device '%s' could not be found" % deviceId)

    def insert(self, deviceId, deviceDetails):
        self._ensure_db_exists()
        return self.client.CreateDocument(self.COLLECTION, deviceDetails)

repository = Repository(os.environ["PAPAYA_DOCDB_HOST"], os.environ["PAPAYA_DOCDB_KEY"])
