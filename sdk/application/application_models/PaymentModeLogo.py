"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class PaymentModeLogo(Schema):

    
    large = fields.Str(required=False)
    
    small = fields.Str(required=False)
    

