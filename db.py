import json
from tinydb import TinyDB, Query

class DB:
    def __init__(self):
         self.db = TinyDB('db.json')

    def saveResource(self, resourceName, resourceId, jsonResource):
        search = Query()
        result = self.db.get((search._resourceName == resourceName) & (search._resourceId == resourceId))
        if (result):
            self.deleteResource(resourceName, resourceId)
        jsonResource["_resourceName"] = resourceName
        jsonResource["_resourceId"] = resourceId
        self.db.insert(jsonResource)

    def findResource(self, resourceName, resourceId):
        search = Query()
        result = self.db.get((search._resourceName == resourceName) & (search._resourceId == resourceId))
        if result:
            result.pop("_resourceName")
            result.pop("_resourceId")
        return result

    def deleteResource(self, resourceName, resourceId):
        search = Query()
        self.db.remove((search._resourceName == resourceName) & (search._resourceId == resourceId))




