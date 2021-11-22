"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *












class OrderDiscountRuleBucket(Schema):

    
    high = fields.Float(required=False)
    
    low = fields.Float(required=False)
    
    max = fields.Float(required=False)
    
    value = fields.Float(required=False)
    
    value_type = fields.Str(required=False)
    

