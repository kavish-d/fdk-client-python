"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .Page import Page

from .CouponAdd import CouponAdd


class CouponsResponse(BaseSchema):
    # Cart swagger.json

    
    page = fields.Nested(Page, required=False)
    
    items = fields.Nested(CouponAdd, required=False)
    

