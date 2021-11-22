"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

class CommonValidator:
    
    class getLocations(Schema):
        
        location_type = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    