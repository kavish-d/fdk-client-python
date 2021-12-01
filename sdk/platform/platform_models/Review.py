"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema





from .MediaMeta import MediaMeta



from .MediaMeta import MediaMeta




class Review(BaseSchema):

    
    description = fields.Str(required=False)
    
    header = fields.Str(required=False)
    
    image_meta = fields.Nested(MediaMeta, required=False)
    
    title = fields.Str(required=False)
    
    video_meta = fields.Nested(MediaMeta, required=False)
    
    vote_allowed = fields.Boolean(required=False)
    

