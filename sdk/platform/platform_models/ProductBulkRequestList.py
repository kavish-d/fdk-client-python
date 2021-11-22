"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .Page import Page

from .ProductBulkRequest import ProductBulkRequest


class ProductBulkRequestList(Schema):

    
    page = fields.Nested(Page, required=False)
    
    items = fields.Nested(ProductBulkRequest, required=False)
    

