"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class Phone(BaseSchema):

    
    phone_number = fields.Str(required=False)
    
    phone_country_code = fields.Str(required=False)
    

