"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *









from .OtherSellerCompany import OtherSellerCompany




class OtherSellerApplication(Schema):

    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    domain = fields.Str(required=False)
    
    company = fields.Nested(OtherSellerCompany, required=False)
    
    opt_type = fields.Str(required=False)
    

