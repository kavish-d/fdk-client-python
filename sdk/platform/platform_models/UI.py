"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *



from .UIIcon import UIIcon






class UI(Schema):

    
    feedback_question = fields.List(fields.Str(required=False), required=False)
    
    icon = fields.Nested(UIIcon, required=False)
    
    text = fields.List(fields.Str(required=False), required=False)
    
    type = fields.Str(required=False)
    

