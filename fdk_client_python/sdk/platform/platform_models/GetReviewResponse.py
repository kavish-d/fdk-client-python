"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .ReviewFacet import ReviewFacet



from .Page import Page

from .SortMethod import SortMethod


class GetReviewResponse(BaseSchema):

    
    facets = fields.List(fields.Nested(ReviewFacet, required=False), required=False)
    
    items = fields.List(fields.Dict(required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    sort = fields.List(fields.Nested(SortMethod, required=False), required=False)
    

