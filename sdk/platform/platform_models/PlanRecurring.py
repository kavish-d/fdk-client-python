"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class PlanRecurring(Schema):

    
    interval = fields.Str(required=False)
    
    interval_count = fields.Float(required=False)
    

