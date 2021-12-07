"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema



from .Time import Time



from .Time import Time


class StoreTiming(BaseSchema):

    
    open = fields.Boolean(required=False)
    
    opening = fields.Nested(Time, required=False)
    
    weekday = fields.Str(required=False)
    
    closing = fields.Nested(Time, required=False)
    

