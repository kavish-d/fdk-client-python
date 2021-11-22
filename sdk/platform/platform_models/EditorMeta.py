"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *










class EditorMeta(Schema):

    
    foreground_color = fields.Str(required=False)
    
    background_color = fields.Str(required=False)
    
    content_type = fields.Str(required=False)
    
    content = fields.Str(required=False)
    

