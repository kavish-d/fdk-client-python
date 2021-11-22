"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class Entity(Schema):

    
    id = fields.Str(required=False)
    
    type = fields.Str(required=False)
    

