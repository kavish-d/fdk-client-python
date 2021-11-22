"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class InventoryBrand(Schema):

    
    criteria = fields.Str(required=False)
    
    brands = fields.List(fields.Raw(required=False), required=False)
    

