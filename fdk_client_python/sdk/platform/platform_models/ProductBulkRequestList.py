"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .ProductBulkRequest import ProductBulkRequest

from .Page import Page


class ProductBulkRequestList(BaseSchema):

    
    items = fields.Nested(ProductBulkRequest, required=False)
    
    page = fields.Nested(Page, required=False)
    

