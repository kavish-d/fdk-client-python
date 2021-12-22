"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class OrderQuantity(BaseSchema):
    # Catalog swagger.json

    
    minimum = fields.Int(required=False)
    
    is_set = fields.Boolean(required=False)
    
    maximum = fields.Int(required=False)
    

