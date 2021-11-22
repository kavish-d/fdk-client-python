"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *










class State(Schema):

    
    active = fields.Boolean(required=False)
    
    approve = fields.Boolean(required=False)
    
    auto_decided = fields.Boolean(required=False)
    
    status = fields.Int(required=False)
    

