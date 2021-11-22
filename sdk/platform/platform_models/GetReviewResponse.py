"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .ReviewFacet import ReviewFacet



from .Page import Page

from .SortMethod import SortMethod


class GetReviewResponse(Schema):

    
    facets = fields.List(fields.Nested(ReviewFacet, required=False), required=False)
    
    items = fields.List(fields.Dict(required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    sort = fields.List(fields.Nested(SortMethod, required=False), required=False)
    

