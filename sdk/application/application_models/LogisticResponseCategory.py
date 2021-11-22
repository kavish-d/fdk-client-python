"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class LogisticResponseCategory(Schema):

    
    id = fields.Int(required=False)
    
    level = fields.Str(required=False)
    

