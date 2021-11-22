"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .Media1 import Media1





from .ActionPage import ActionPage


class ProductBrand(Schema):

    
    logo = fields.Nested(Media1, required=False)
    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    action = fields.Nested(ActionPage, required=False)
    

