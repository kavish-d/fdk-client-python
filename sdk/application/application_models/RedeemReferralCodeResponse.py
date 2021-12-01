"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema












class RedeemReferralCodeResponse(BaseSchema):

    
    message = fields.Str(required=False)
    
    points = fields.Float(required=False)
    
    redeemed = fields.Boolean(required=False)
    
    referrer_id = fields.Str(required=False)
    
    referrer_info = fields.Str(required=False)
    

