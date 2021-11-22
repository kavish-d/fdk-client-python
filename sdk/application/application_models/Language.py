"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class Language(Schema):

    
    display = fields.Str(required=False)
    

