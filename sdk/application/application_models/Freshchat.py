"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .FreshchatCredentials import FreshchatCredentials




class Freshchat(Schema):

    
    credentials = fields.Nested(FreshchatCredentials, required=False)
    
    enabled = fields.Boolean(required=False)
    

