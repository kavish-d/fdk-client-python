"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class EditMobileRequestSchema(Schema):

    
    country_code = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    

