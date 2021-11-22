"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *












class CouponValidity(Schema):

    
    display_message_en = fields.Str(required=False)
    
    discount = fields.Float(required=False)
    
    valid = fields.Boolean(required=False)
    
    code = fields.Str(required=False)
    
    title = fields.Str(required=False)
    

