"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class SellerPhoneNumber(Schema):

    
    number = fields.Str(required=False)
    
    country_code = fields.Int(required=False)
    

