"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .ProductStockStatusItem import ProductStockStatusItem


class ProductStockStatusResponse(BaseSchema):

    
    items = fields.List(fields.Nested(ProductStockStatusItem, required=False), required=False)
    

