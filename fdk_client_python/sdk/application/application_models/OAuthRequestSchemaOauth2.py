"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema








class OAuthRequestSchemaOauth2(BaseSchema):

    
    access_token = fields.Str(required=False)
    
    expiry = fields.Int(required=False)
    
    refresh_token = fields.Str(required=False)
    

