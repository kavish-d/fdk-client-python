"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .Page import Page

from .Product import Product


class ProductListingResponse(Schema):

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(Product, required=False), required=False)
    

