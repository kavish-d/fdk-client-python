"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class OpenApiFiles(Schema):

    
    key = fields.Str(required=False)
    
    values = fields.List(fields.Str(required=False), required=False)
    

