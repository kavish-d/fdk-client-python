"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class TokenRequestBodySchema(Schema):

    
    token = fields.Str(required=False)
    

