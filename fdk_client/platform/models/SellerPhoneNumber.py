"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class SellerPhoneNumber(BaseSchema):
    # CompanyProfile swagger.json

    
    country_code = fields.Int(required=False)
    
    number = fields.Str(required=False)
    

