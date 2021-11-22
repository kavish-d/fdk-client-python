"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .ProductStockStatusItem import ProductStockStatusItem


class ProductStockStatusResponse(Schema):

    
    items = fields.List(fields.Nested(ProductStockStatusItem, required=False), required=False)
    

