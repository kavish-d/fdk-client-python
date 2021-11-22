"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .Opening import Opening





from .Closing import Closing


class Timing(Schema):

    
    opening = fields.Nested(Opening, required=False)
    
    weekday = fields.Str(required=False)
    
    open = fields.Boolean(required=False)
    
    closing = fields.Nested(Closing, required=False)
    

