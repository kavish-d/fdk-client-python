"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class OS(Schema):

    
    name = fields.Str(required=False)
    
    version = fields.Str(required=False)
    

