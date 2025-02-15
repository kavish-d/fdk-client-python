"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema














class CouponBreakup(BaseSchema):
    # Cart swagger.json

    
    type = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    value = fields.Float(required=False)
    
    is_applied = fields.Boolean(required=False)
    
    code = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    

