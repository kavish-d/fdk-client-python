"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class OAuthRequestAppleSchemaOauth(Schema):

    
    identity_token = fields.Str(required=False)
    

