"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class Login(Schema):

    
    password = fields.Boolean(required=False)
    
    otp = fields.Boolean(required=False)
    

