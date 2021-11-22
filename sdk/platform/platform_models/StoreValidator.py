"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .JsonSchema import JsonSchema




class StoreValidator(Schema):

    
    json_schema = fields.List(fields.Nested(JsonSchema, required=False), required=False)
    
    browser_script = fields.Str(required=False)
    

