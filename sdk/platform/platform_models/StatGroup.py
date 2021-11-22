"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *








class StatGroup(Schema):

    
    key = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    title = fields.Str(required=False)
    

