"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema




class GtmCredentials(BaseSchema):
    # Configuration swagger.json

    
    api_key = fields.Str(required=False)
    

