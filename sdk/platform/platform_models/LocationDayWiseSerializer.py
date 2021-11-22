"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *



from .LocationTimingSerializer import LocationTimingSerializer

from .LocationTimingSerializer import LocationTimingSerializer




class LocationDayWiseSerializer(Schema):

    
    open = fields.Boolean(required=False)
    
    closing = fields.Nested(LocationTimingSerializer, required=False)
    
    opening = fields.Nested(LocationTimingSerializer, required=False)
    
    weekday = fields.Str(required=False)
    

