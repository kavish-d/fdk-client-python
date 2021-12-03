"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class InventoryDiscount(BaseSchema):

    
    min = fields.Float(required=False)
    
    max = fields.Float(required=False)
    

