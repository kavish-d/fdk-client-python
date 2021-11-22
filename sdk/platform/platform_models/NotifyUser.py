"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class NotifyUser(Schema):

    
    country_code = fields.Str(required=False)
    
    phone_number = fields.Str(required=False)
    

