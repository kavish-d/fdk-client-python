"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class NotFoundSchema(Schema):

    
    message = fields.Str(required=False)
    

