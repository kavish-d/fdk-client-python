"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *












class Price(Schema):

    
    min_marked = fields.Float(required=False)
    
    min_effective = fields.Float(required=False)
    
    currency = fields.Str(required=False)
    
    max_marked = fields.Float(required=False)
    
    max_effective = fields.Float(required=False)
    

