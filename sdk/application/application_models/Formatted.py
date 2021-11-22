"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class Formatted(Schema):

    
    min = fields.Str(required=False)
    
    max = fields.Str(required=False)
    

