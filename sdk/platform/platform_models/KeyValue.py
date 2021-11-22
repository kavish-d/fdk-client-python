"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class KeyValue(Schema):

    
    key = fields.Str(required=False)
    
    value = fields.Dict(required=False)
    

