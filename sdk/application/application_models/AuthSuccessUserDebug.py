"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class AuthSuccessUserDebug(Schema):

    
    platform = fields.Str(required=False)
    

