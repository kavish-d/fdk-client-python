"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema











from .Action import Action


class SlideshowMedia(BaseSchema):

    
    type = fields.Str(required=False)
    
    url = fields.Str(required=False)
    
    bg_color = fields.Str(required=False)
    
    duration = fields.Int(required=False)
    
    auto_decide_duration = fields.Boolean(required=False)
    
    action = fields.Nested(Action, required=False)
    
