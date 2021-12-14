"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema




class OAuthRequestAppleSchemaOauth(BaseSchema):
    # User swagger.json

    
    identity_token = fields.Str(required=False)
    

