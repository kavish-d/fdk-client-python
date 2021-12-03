"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .ProductSizePriceResponse import ProductSizePriceResponse

from .ProductSizeSellerFilter import ProductSizeSellerFilter

from .Page import Page


class ProductSizeSellersResponse(BaseSchema):

    
    items = fields.List(fields.Nested(ProductSizePriceResponse, required=False), required=False)
    
    sort_on = fields.List(fields.Nested(ProductSizeSellerFilter, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

