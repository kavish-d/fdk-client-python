"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class Css(Schema):

    
    link = fields.Str(required=False)
    

