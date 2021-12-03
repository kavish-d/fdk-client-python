"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class GTIN(BaseSchema):

    
    primary = fields.Boolean(required=False)
    
    gtin_value = fields.Str(required=False)
    
    gtin_type = fields.Str(required=False)
    
