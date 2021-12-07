"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema


























class LimitedProductData(BaseSchema):

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
    sizes = fields.List(fields.Str(required=False), required=False)
    
    country_of_origin = fields.Str(required=False)
    
    price = fields.Dict(required=False)
    
    identifier = fields.Dict(required=False)
    
    attributes = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    short_description = fields.Str(required=False)
    
    item_code = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    images = fields.List(fields.Str(required=False), required=False)
    

