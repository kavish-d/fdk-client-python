"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .Media import Media

from .Media import Media


class ImageUrls(Schema):

    
    landscape = fields.Nested(Media, required=False)
    
    portrait = fields.Nested(Media, required=False)
    

