"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema












class CouponSchedule(BaseSchema):

    
    duration = fields.Int(required=False)
    
    cron = fields.Str(required=False)
    
    start = fields.Str(required=False)
    
    end = fields.Str(required=False)
    
    next_schedule = fields.List(fields.Dict(required=False), required=False)
    

