"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class ProductSortOn(BaseSchema):

    
    value = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    is_selected = fields.Boolean(required=False)
    

