"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .Page import Page

from .GetCollectionDetailNest import GetCollectionDetailNest

from .CollectionListingFilter import CollectionListingFilter


class GetCollectionListingResponse(Schema):

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(GetCollectionDetailNest, required=False), required=False)
    
    filters = fields.Nested(CollectionListingFilter, required=False)
    

