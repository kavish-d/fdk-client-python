"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema




class OAuthRequestAppleSchemaOauth(BaseSchema):

    
    identity_token = fields.Str(required=False)
    
