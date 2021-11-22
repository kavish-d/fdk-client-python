"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .Page import Page

from .ProductStockStatusItem import ProductStockStatusItem


class ProductStockPolling(Schema):

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(ProductStockStatusItem, required=False), required=False)
    

