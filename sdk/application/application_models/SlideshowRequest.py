"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *





from .ConfigurationSchema import ConfigurationSchema

from .SlideshowMedia import SlideshowMedia




class SlideshowRequest(Schema):

    
    slug = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    
    configuration = fields.Nested(ConfigurationSchema, required=False)
    
    media = fields.Nested(SlideshowMedia, required=False)
    
    active = fields.Boolean(required=False)
    

