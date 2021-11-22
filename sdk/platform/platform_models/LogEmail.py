"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class LogEmail(Schema):

    
    template = fields.Str(required=False)
    

