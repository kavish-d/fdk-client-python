"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .ProductDownloadsItems import ProductDownloadsItems

from .Page import Page


class ProductDownloadsResponse(BaseSchema):

    
    items = fields.Nested(ProductDownloadsItems, required=False)
    
    page = fields.Nested(Page, required=False)
    

