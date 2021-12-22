"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .Page import Page

from .ProductSizeSellerFilter import ProductSizeSellerFilter

from .ProductSizePriceResponse import ProductSizePriceResponse


class ProductSizeSellersResponse(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(Page, required=False)
    
    sort_on = fields.List(fields.Nested(ProductSizeSellerFilter, required=False), required=False)
    
    items = fields.List(fields.Nested(ProductSizePriceResponse, required=False), required=False)
    

