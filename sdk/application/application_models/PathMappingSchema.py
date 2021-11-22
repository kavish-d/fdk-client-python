"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *



from .RedirectionSchema import RedirectionSchema








class PathMappingSchema(Schema):

    
    application = fields.Str(required=False)
    
    redirections = fields.List(fields.Nested(RedirectionSchema, required=False), required=False)
    
    _id = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    

