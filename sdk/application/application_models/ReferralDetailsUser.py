"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *










class ReferralDetailsUser(Schema):

    
    blocked = fields.Boolean(required=False)
    
    points = fields.Float(required=False)
    
    redeemed = fields.Boolean(required=False)
    
    referral_code = fields.Str(required=False)
    

