"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class EditEmailRequestSchema(Schema):

    
    email = fields.Str(required=False)
    

