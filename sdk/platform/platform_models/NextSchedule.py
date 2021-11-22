"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class NextSchedule(Schema):

    
    start = fields.Str(required=False)
    
    end = fields.Str(required=False)
    

