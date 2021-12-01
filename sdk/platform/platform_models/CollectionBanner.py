"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .CollectionImage import CollectionImage

from .CollectionImage import CollectionImage


class CollectionBanner(BaseSchema):

    
    landscape = fields.Nested(CollectionImage, required=False)
    
    portrait = fields.Nested(CollectionImage, required=False)
    

