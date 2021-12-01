"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class InventoryCategory(BaseSchema):

    
    criteria = fields.Str(required=False)
    
    categories = fields.List(fields.Raw(required=False), required=False)
    

