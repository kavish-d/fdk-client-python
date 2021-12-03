"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema



from .ActionPage import ActionPage



from .Media1 import Media1


class ProductBrand(BaseSchema):

    
    name = fields.Str(required=False)
    
    action = fields.Nested(ActionPage, required=False)
    
    uid = fields.Int(required=False)
    
    logo = fields.Nested(Media1, required=False)
    

