"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .Page import Page

from .GetProductBundleCreateResponse import GetProductBundleCreateResponse


class GetProductBundleListingResponse(Schema):

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(GetProductBundleCreateResponse, required=False), required=False)
    

