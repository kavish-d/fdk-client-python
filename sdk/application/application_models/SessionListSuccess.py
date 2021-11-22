"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class SessionListSuccess(Schema):

    
    sessions = fields.List(fields.Str(required=False), required=False)
    

