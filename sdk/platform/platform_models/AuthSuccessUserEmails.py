"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *










class AuthSuccessUserEmails(Schema):

    
    email = fields.Str(required=False)
    
    verified = fields.Boolean(required=False)
    
    primary = fields.Boolean(required=False)
    
    active = fields.Boolean(required=False)
    

