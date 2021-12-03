"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema
































class ShippingAddress(BaseSchema):

    
    phone = fields.Int(required=False)
    
    area = fields.Str(required=False)
    
    area_code_slug = fields.Str(required=False)
    
    landmark = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    area_code = fields.Str(required=False)
    
    state = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    address = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    address_type = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
