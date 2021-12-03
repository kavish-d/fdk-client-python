"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema











from .EntityRequest import EntityRequest

from .RatingRequest import RatingRequest

from .ReviewRequest import ReviewRequest


class TemplateRequest(BaseSchema):

    
    active = fields.Boolean(required=False)
    
    enable_media_type = fields.Str(required=False)
    
    enable_qna = fields.Boolean(required=False)
    
    enable_rating = fields.Boolean(required=False)
    
    enable_review = fields.Boolean(required=False)
    
    entity = fields.Nested(EntityRequest, required=False)
    
    rating = fields.Nested(RatingRequest, required=False)
    
    review = fields.Nested(ReviewRequest, required=False)
    

