"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class UnhandledError(Schema):

    
    message = fields.Str(required=False)
    

