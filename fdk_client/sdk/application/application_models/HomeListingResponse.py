"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .Page import Page



from .ProductListingDetail import ProductListingDetail


class HomeListingResponse(BaseSchema):
    # Catalog swagger.json

    
    page = fields.Nested(Page, required=False)
    
    message = fields.Str(required=False)
    
    items = fields.List(fields.Nested(ProductListingDetail, required=False), required=False)
    

