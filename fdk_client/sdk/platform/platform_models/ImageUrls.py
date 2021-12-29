"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .BannerImage import BannerImage

from .BannerImage import BannerImage


class ImageUrls(BaseSchema):
    # Catalog swagger.json

    
    landscape = fields.Nested(BannerImage, required=False)
    
    portrait = fields.Nested(BannerImage, required=False)
    

