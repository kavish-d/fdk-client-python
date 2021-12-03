"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .CollectionListingFilterTag import CollectionListingFilterTag

from .CollectionListingFilterType import CollectionListingFilterType


class CollectionListingFilter(BaseSchema):

    
    tags = fields.List(fields.Nested(CollectionListingFilterTag, required=False), required=False)
    
    type = fields.List(fields.Nested(CollectionListingFilterType, required=False), required=False)
    

