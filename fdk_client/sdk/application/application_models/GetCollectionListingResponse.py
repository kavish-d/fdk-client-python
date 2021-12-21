"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .GetCollectionDetailNest import GetCollectionDetailNest

from .Page import Page

from .CollectionListingFilter import CollectionListingFilter


class GetCollectionListingResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.List(fields.Nested(GetCollectionDetailNest, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    
    filters = fields.Nested(CollectionListingFilter, required=False)
    

