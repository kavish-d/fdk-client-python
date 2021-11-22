"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *












class CreateUserSessionResponseSchema(Schema):

    
    domain = fields.Str(required=False)
    
    max_age = fields.Float(required=False)
    
    secure = fields.Boolean(required=False)
    
    http_only = fields.Boolean(required=False)
    
    cookie = fields.Dict(required=False)
    

