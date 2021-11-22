"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .PageResponse import PageResponse

from .HsnCodesObject import HsnCodesObject


class HsnCodesListingResponse(Schema):

    
    page = fields.Nested(PageResponse, required=False)
    
    items = fields.List(fields.Nested(HsnCodesObject, required=False), required=False)
    

