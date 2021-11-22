"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *







from .MediaMeta import MediaMeta




class Review(Schema):

    
    answer_ids = fields.List(fields.Str(required=False), required=False)
    
    comments = fields.List(fields.Str(required=False), required=False)
    
    description = fields.Str(required=False)
    
    media_meta = fields.List(fields.Nested(MediaMeta, required=False), required=False)
    
    title = fields.Str(required=False)
    

