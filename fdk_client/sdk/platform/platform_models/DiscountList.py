"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .DiscountDetail import DiscountDetail

from .Page import Page


class DiscountList(BaseSchema):
    # Discount swagger.json

    
    items = fields.List(fields.Nested(DiscountDetail, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
