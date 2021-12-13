"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema





from .Media1 import Media1

from .ActionPage import ActionPage


class ProductBrand(BaseSchema):

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    logo = fields.Nested(Media1, required=False)
    
    action = fields.Nested(ActionPage, required=False)
    

