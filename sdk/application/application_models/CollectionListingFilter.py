"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .CollectionListingFilterTag import CollectionListingFilterTag

from .CollectionListingFilterType import CollectionListingFilterType


class CollectionListingFilter(Schema):

    
    tags = fields.List(fields.Nested(CollectionListingFilterTag, required=False), required=False)
    
    type = fields.List(fields.Nested(CollectionListingFilterType, required=False), required=False)
    

