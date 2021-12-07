"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .DisplayBreakup import DisplayBreakup

from .RawBreakup import RawBreakup

from .LoyaltyPoints import LoyaltyPoints

from .CouponBreakup import CouponBreakup


class CartBreakup(BaseSchema):

    
    display = fields.List(fields.Nested(DisplayBreakup, required=False), required=False)
    
    raw = fields.Nested(RawBreakup, required=False)
    
    loyalty_points = fields.Nested(LoyaltyPoints, required=False)
    
    coupon = fields.Nested(CouponBreakup, required=False)
    

