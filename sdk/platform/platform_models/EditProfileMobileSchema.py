"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class EditProfileMobileSchema(Schema):

    
    phone = fields.Str(required=False)
    
    country_code = fields.Str(required=False)
    

