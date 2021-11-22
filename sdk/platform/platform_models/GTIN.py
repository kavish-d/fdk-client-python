"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *








class GTIN(Schema):

    
    gtin_value = fields.Str(required=False)
    
    gtin_type = fields.Str(required=False)
    
    primary = fields.Boolean(required=False)
    

