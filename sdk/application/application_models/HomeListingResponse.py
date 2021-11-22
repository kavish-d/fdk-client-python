"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *



from .Page import Page

from .ProductListingDetail import ProductListingDetail


class HomeListingResponse(Schema):

    
    message = fields.Str(required=False)
    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(ProductListingDetail, required=False), required=False)
    

