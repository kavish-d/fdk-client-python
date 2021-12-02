"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .LoyaltyPoints import LoyaltyPoints

from .CouponBreakup import CouponBreakup

from .RawBreakup import RawBreakup

from .DisplayBreakup import DisplayBreakup


class CartBreakup(BaseSchema):

    
    loyalty_points = fields.Nested(LoyaltyPoints, required=False)
    
    coupon = fields.Nested(CouponBreakup, required=False)
    
    raw = fields.Nested(RawBreakup, required=False)
    
    display = fields.List(fields.Nested(DisplayBreakup, required=False), required=False)
    

