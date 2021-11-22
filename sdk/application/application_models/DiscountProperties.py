"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *












class DiscountProperties(Schema):

    
    absolute = fields.Float(required=False)
    
    currency = fields.Str(required=False)
    
    display_absolute = fields.Str(required=False)
    
    display_percent = fields.Str(required=False)
    
    percent = fields.Float(required=False)
    

