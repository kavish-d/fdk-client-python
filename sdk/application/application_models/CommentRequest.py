"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema








class CommentRequest(BaseSchema):

    
    comment = fields.List(fields.Str(required=False), required=False)
    
    entity_id = fields.Str(required=False)
    
    entity_type = fields.Str(required=False)
    

