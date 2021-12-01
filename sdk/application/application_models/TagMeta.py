"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .MediaMeta import MediaMeta






class TagMeta(BaseSchema):

    
    media = fields.List(fields.Nested(MediaMeta, required=False), required=False)
    
    name = fields.Str(required=False)
    
    type = fields.Str(required=False)
    

