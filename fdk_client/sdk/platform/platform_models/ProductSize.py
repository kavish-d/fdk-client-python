"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class ProductSize(BaseSchema):

    
    max = fields.Int(required=False)
    
    min = fields.Int(required=False)
    

