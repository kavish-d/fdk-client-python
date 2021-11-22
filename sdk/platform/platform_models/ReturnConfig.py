"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *








class ReturnConfig(Schema):

    
    time = fields.Int(required=False)
    
    returnable = fields.Boolean(required=False)
    
    unit = fields.Str(required=False)
    

