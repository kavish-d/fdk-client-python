"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *












class UpdateQNARequest(Schema):

    
    active = fields.Boolean(required=False)
    
    approve = fields.Boolean(required=False)
    
    choices = fields.List(fields.Str(required=False), required=False)
    
    id = fields.Str(required=False)
    
    tags = fields.List(fields.Str(required=False), required=False)
    

