"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *



from .OAuthRequestSchemaOauth2 import OAuthRequestSchemaOauth2

from .OAuthRequestSchemaProfile import OAuthRequestSchemaProfile


class OAuthRequestSchema(Schema):

    
    is_signed_in = fields.Boolean(required=False)
    
    oauth2 = fields.Nested(OAuthRequestSchemaOauth2, required=False)
    
    profile = fields.Nested(OAuthRequestSchemaProfile, required=False)
    

