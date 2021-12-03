"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema










class State(BaseSchema):

    
    active = fields.Boolean(required=False)
    
    approve = fields.Boolean(required=False)
    
    auto_decided = fields.Boolean(required=False)
    
    status = fields.Int(required=False)
    
