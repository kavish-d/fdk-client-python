"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class ApplyCouponRequest(Schema):

    
    coupon_code = fields.Str(required=False)
    

