"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class LocationDefaultLanguage(BaseSchema):
    # Common swagger.json

    
    name = fields.Str(required=False)
    
    code = fields.Str(required=False)
    

