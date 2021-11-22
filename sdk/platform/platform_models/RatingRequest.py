"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *



from .UI import UI


class RatingRequest(Schema):

    
    attributes = fields.List(fields.Str(required=False), required=False)
    
    ui = fields.Nested(UI, required=False)
    

