"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class OtherSellerCompany(Schema):

    
    uid = fields.Int(required=False)
    
    name = fields.Str(required=False)
    

