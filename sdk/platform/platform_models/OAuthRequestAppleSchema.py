"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *



from .OAuthRequestAppleSchemaOauth import OAuthRequestAppleSchemaOauth

from .OAuthRequestAppleSchemaProfile import OAuthRequestAppleSchemaProfile


class OAuthRequestAppleSchema(Schema):

    
    user_identifier = fields.Str(required=False)
    
    oauth = fields.Nested(OAuthRequestAppleSchemaOauth, required=False)
    
    profile = fields.Nested(OAuthRequestAppleSchemaProfile, required=False)
    

