"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema












class CouponValidity(BaseSchema):

    
    valid = fields.Boolean(required=False)
    
    title = fields.Str(required=False)
    
    discount = fields.Float(required=False)
    
    code = fields.Str(required=False)
    
    display_message_en = fields.Str(required=False)
    

