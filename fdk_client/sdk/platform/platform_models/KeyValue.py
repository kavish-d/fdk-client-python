"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class KeyValue(BaseSchema):

    
    key = fields.Str(required=False)
    
    value = fields.Dict(required=False)
    

