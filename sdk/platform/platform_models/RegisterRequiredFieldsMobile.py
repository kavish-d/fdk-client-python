"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class RegisterRequiredFieldsMobile(Schema):

    
    is_required = fields.Boolean(required=False)
    
    level = fields.Str(required=False)
    

