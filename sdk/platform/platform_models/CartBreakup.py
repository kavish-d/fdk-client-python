"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .LoyaltyPoints import LoyaltyPoints

from .DisplayBreakup import DisplayBreakup

from .CouponBreakup import CouponBreakup

from .RawBreakup import RawBreakup


class CartBreakup(Schema):

    
    loyalty_points = fields.Nested(LoyaltyPoints, required=False)
    
    display = fields.List(fields.Nested(DisplayBreakup, required=False), required=False)
    
    coupon = fields.Nested(CouponBreakup, required=False)
    
    raw = fields.Nested(RawBreakup, required=False)
    

