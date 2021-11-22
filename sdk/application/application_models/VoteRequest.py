"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *












class VoteRequest(Schema):

    
    action = fields.Str(required=False)
    
    entity_id = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    
    ref_id = fields.Str(required=False)
    
    ref_type = fields.Str(required=False)
    

