"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class SuccessMessageResponse(Schema):

    
    message = fields.Str(required=False)
    

