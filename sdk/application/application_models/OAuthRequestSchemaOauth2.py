"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *








class OAuthRequestSchemaOauth2(Schema):

    
    access_token = fields.Str(required=False)
    
    expiry = fields.Int(required=False)
    
    refresh_token = fields.Str(required=False)
    

