"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class ApplicationSchema(Schema):

    
    id = fields.Str(required=False)
    

