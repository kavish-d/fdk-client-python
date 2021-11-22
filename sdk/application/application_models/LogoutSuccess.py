"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class LogoutSuccess(Schema):

    
    logout = fields.Boolean(required=False)
    

