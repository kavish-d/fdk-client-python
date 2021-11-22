"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class PaymentModeLogo(Schema):

    
    small = fields.Str(required=False)
    
    large = fields.Str(required=False)
    

