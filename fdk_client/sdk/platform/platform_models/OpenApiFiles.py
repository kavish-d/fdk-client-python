"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class OpenApiFiles(BaseSchema):

    
    key = fields.Str(required=False)
    
    values = fields.List(fields.Str(required=False), required=False)
    

