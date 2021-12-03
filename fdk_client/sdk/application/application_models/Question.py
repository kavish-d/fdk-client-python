"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema










class Question(BaseSchema):

    
    choices = fields.List(fields.Str(required=False), required=False)
    
    max_len = fields.Int(required=False)
    
    text = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
