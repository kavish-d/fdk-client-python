"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema



from .CouponSchedule import CouponSchedule


class CouponPartialUpdate(BaseSchema):

    
    archive = fields.Boolean(required=False)
    
    schedule = fields.Nested(CouponSchedule, required=False)
    

