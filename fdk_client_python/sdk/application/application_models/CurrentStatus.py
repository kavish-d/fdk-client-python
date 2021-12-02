"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema










class CurrentStatus(BaseSchema):

    
    updated_at = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    journey_type = fields.Str(required=False)
    

