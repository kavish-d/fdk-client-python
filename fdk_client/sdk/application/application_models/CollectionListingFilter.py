"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .CollectionListingFilterType import CollectionListingFilterType

from .CollectionListingFilterTag import CollectionListingFilterTag


class CollectionListingFilter(BaseSchema):

    
    type = fields.List(fields.Nested(CollectionListingFilterType, required=False), required=False)
    
    tags = fields.List(fields.Nested(CollectionListingFilterTag, required=False), required=False)
    
