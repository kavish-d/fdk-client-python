"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class Src(Schema):

    
    link = fields.Str(required=False)
    

