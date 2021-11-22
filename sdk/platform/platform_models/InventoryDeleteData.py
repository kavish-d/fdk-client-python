"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *








class InventoryDeleteData(Schema):

    
    item_id = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
    location_id = fields.Int(required=False)
    

