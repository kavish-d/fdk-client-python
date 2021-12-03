"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema





from .MediaMetaRequest import MediaMetaRequest





from .MediaMetaRequest import MediaMetaRequest


class ReviewRequest(BaseSchema):

    
    description = fields.Str(required=False)
    
    header = fields.Str(required=False)
    
    image_meta = fields.Nested(MediaMetaRequest, required=False)
    
    is_vote_allowed = fields.Boolean(required=False)
    
    title = fields.Str(required=False)
    
    video_meta = fields.Nested(MediaMetaRequest, required=False)
    

