"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






















class OAuthConfig(BaseSchema):
    # Inventory swagger.json

    
    limit = fields.Int(required=False)
    
    pages = fields.Int(required=False)
    
    interval = fields.Int(required=False)
    
    consumer_key = fields.Str(required=False)
    
    consumer_secret = fields.Str(required=False)
    
    token = fields.Str(required=False)
    
    token_secret = fields.Str(required=False)
    
    rest_url = fields.Str(required=False)
    
    rest_base_url = fields.Str(required=False)
    
    function_name = fields.Str(required=False)
    

