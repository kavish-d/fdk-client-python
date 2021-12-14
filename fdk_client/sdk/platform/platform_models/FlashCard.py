"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class FlashCard(BaseSchema):
    # User swagger.json

    
    text = fields.Str(required=False)
    
    text_color = fields.Str(required=False)
    
    background_color = fields.Str(required=False)
    

