"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .GetProductBundleCreateResponse import GetProductBundleCreateResponse

from .Page import Page


class GetProductBundleListingResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(GetProductBundleCreateResponse, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

