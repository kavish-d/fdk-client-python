"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class SellerPhoneNumber(BaseSchema):

    
    number = fields.Str(required=False)
    
    country_code = fields.Int(required=False)
    

