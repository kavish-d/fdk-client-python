"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class Phone(Schema):

    
    phone_number = fields.Str(required=False)
    
    phone_country_code = fields.Str(required=False)
    

