"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class InvalidPayloadRequest(Schema):

    
    message = fields.Str(required=False)
    

