"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .Size1 import Size1






class InventoryBulkRequest(BaseSchema):
    # Catalog swagger.json

    
    company_id = fields.Int(required=False)
    
    sizes = fields.List(fields.Nested(Size1, required=False), required=False)
    
    batch_id = fields.Str(required=False)
    
    user = fields.Dict(required=False)
    

