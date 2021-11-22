"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .CollectionListingFilterType import CollectionListingFilterType

from .CollectionListingFilterTag import CollectionListingFilterTag


class CollectionListingFilter(Schema):

    
    type = fields.List(fields.Nested(CollectionListingFilterType, required=False), required=False)
    
    tags = fields.List(fields.Nested(CollectionListingFilterTag, required=False), required=False)
    

