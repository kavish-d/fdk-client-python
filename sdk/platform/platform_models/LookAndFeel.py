"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class LookAndFeel(Schema):

    
    card_position = fields.Str(required=False)
    
    background_color = fields.Str(required=False)
    

