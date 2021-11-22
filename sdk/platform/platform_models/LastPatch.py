"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *








class LastPatch(Schema):

    
    op = fields.Str(required=False)
    
    path = fields.Str(required=False)
    
    value = fields.Str(required=False)
    

