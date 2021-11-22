"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .DiscountJob import DiscountJob

from .Page import Page


class ListOrCalender(Schema):

    
    items = fields.List(fields.Nested(DiscountJob, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

