"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema












class UpdateVoteRequest(BaseSchema):

    
    action = fields.Str(required=False)
    
    active = fields.Boolean(required=False)
    
    id = fields.Str(required=False)
    
    ref_id = fields.Str(required=False)
    
    ref_type = fields.Str(required=False)
    

