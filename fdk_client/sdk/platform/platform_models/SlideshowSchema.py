"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema





from .DateMeta import DateMeta





from .ConfigurationSchema import ConfigurationSchema

from .SlideshowMedia import SlideshowMedia








class SlideshowSchema(BaseSchema):

    
    _id = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    date_meta = fields.Nested(DateMeta, required=False)
    
    application = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    
    configuration = fields.Nested(ConfigurationSchema, required=False)
    
    media = fields.List(fields.Nested(SlideshowMedia, required=False), required=False)
    
    active = fields.Boolean(required=False)
    
    archived = fields.Boolean(required=False)
    
    _custom_json = fields.Dict(required=False)
    

