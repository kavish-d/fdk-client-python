"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema










class EditorMeta(BaseSchema):

    
    foreground_color = fields.Str(required=False)
    
    background_color = fields.Str(required=False)
    
    content_type = fields.Str(required=False)
    
    content = fields.Str(required=False)
    

