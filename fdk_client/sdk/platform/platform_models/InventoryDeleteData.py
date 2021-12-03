"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class InventoryDeleteData(BaseSchema):

    
    size = fields.Str(required=False)
    
    item_id = fields.Int(required=False)
    
    location_id = fields.Int(required=False)
    
