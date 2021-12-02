"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema





from .Size1 import Size1




class InventoryBulkRequest(BaseSchema):

    
    company_id = fields.Int(required=False)
    
    user = fields.Dict(required=False)
    
    sizes = fields.List(fields.Nested(Size1, required=False), required=False)
    
    batch_id = fields.Str(required=False)
    

