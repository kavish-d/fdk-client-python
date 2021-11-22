"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .CollectionImage import CollectionImage

from .CollectionImage import CollectionImage


class CollectionBanner(Schema):

    
    landscape = fields.Nested(CollectionImage, required=False)
    
    portrait = fields.Nested(CollectionImage, required=False)
    

