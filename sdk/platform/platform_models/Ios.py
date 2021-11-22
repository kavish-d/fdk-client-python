"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class Ios(Schema):

    
    application_id = fields.Str(required=False)
    
    api_key = fields.Str(required=False)
    

