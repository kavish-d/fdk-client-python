"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .BannerImage import BannerImage

from .BannerImage import BannerImage


class ImageUrls(Schema):

    
    landscape = fields.Nested(BannerImage, required=False)
    
    portrait = fields.Nested(BannerImage, required=False)
    

