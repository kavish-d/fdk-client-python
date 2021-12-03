"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema
































class BillingAddress(BaseSchema):

    
    address1 = fields.Str(required=False)
    
    city = fields.Str(required=False)
    
    zip = fields.Str(required=False)
    
    last_name = fields.Str(required=False)
    
    address2 = fields.Str(required=False)
    
    latitude = fields.Float(required=False)
    
    longitude = fields.Float(required=False)
    
    province_code = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    
    company = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    country = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    
    first_name = fields.Str(required=False)
    
    province = fields.Str(required=False)
    
