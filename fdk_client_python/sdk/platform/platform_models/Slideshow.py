"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .SlideshowSchema import SlideshowSchema




class Slideshow(BaseSchema):

    
    data = fields.Nested(SlideshowSchema, required=False)
    
    success = fields.Boolean(required=False)
    

