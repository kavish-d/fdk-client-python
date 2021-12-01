"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema




























class HistoryPretty(BaseSchema):

    
    _id = fields.Str(required=False)
    
    application_id = fields.Str(required=False)
    
    claimed = fields.Boolean(required=False)
    
    created_at = fields.Str(required=False)
    
    expires_on = fields.Str(required=False)
    
    points = fields.Float(required=False)
    
    remaining_points = fields.Float(required=False)
    
    text_1 = fields.Str(required=False)
    
    text_2 = fields.Str(required=False)
    
    text_3 = fields.Str(required=False)
    
    txn_name = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    user_id = fields.Str(required=False)
    

