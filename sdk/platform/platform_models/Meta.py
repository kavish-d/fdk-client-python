"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *








class Meta(Schema):

    
    values = fields.List(fields.Dict(required=False), required=False)
    
    headers = fields.Dict(required=False)
    
    unit = fields.Str(required=False)
    

