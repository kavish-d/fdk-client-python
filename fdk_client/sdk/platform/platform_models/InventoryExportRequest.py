"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class InventoryExportRequest(BaseSchema):
    # Catalog swagger.json

    
    brand = fields.List(fields.Int(required=False), required=False)
    
    store = fields.List(fields.Int(required=False), required=False)
    
    type = fields.Str(required=False)
    

