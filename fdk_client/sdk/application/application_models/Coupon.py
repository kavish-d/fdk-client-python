"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






















class Coupon(BaseSchema):

    
    is_applicable = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    title = fields.Str(required=False)
    
    max_discount_value = fields.Float(required=False)
    
    coupon_code = fields.Str(required=False)
    
    sub_title = fields.Str(required=False)
    
    expires_on = fields.Str(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    coupon_value = fields.Float(required=False)
    
    minimum_cart_value = fields.Float(required=False)
    
