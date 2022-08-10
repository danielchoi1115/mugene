from typing import Any, Dict
from pydantic import BaseModel
from bson.son import SON
from bson.objectid import ObjectId
class DBRef(BaseModel):
    collection: str
    object_id: str
    database: str = None
    
    def as_doc(self) -> Dict[str, Any]:
        doc = SON([("$ref", self.collection), ("$id", self.object_id)])
        if self.database is not None:
            doc["$db"] = self.database
        return doc