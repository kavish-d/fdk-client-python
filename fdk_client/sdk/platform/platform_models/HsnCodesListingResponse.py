"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .HsnCodesObject import HsnCodesObject

from .PageResponse import PageResponse


class HsnCodesListingResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(HsnCodesObject, required=False), required=False)
    
    page = fields.Nested(PageResponse, required=False)
    

