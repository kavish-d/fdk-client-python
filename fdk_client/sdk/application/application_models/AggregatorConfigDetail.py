"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






















class AggregatorConfigDetail(BaseSchema):

    
    merchant_key = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    sdk = fields.Boolean(required=False)
    
    merchant_id = fields.Str(required=False)
    
    pin = fields.Str(required=False)
    
    api = fields.Str(required=False)
    
    verify_api = fields.Str(required=False)
    
    secret = fields.Str(required=False)
    
    config_type = fields.Str(required=False)
    
