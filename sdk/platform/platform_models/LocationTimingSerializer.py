"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class LocationTimingSerializer(Schema):

    
    hour = fields.Int(required=False)
    
    minute = fields.Int(required=False)
    

