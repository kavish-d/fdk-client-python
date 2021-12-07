"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .LoyaltyPoints import LoyaltyPoints

from .RawBreakup import RawBreakup

from .DisplayBreakup import DisplayBreakup

from .CouponBreakup import CouponBreakup


class CartBreakup(BaseSchema):

    
    loyalty_points = fields.Nested(LoyaltyPoints, required=False)
    
    raw = fields.Nested(RawBreakup, required=False)
    
    display = fields.List(fields.Nested(DisplayBreakup, required=False), required=False)
    
    coupon = fields.Nested(CouponBreakup, required=False)
    

