"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema







from .Referral import Referral










class RewardUser(BaseSchema):

    
    _id = fields.Str(required=False)
    
    active = fields.Boolean(required=False)
    
    created_at = fields.Str(required=False)
    
    referral = fields.Nested(Referral, required=False)
    
    uid = fields.Int(required=False)
    
    updated_at = fields.Str(required=False)
    
    user_block_reason = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
