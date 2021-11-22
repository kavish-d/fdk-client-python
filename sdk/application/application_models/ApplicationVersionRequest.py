"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *












class ApplicationVersionRequest(Schema):

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    namespace = fields.Str(required=False)
    
    token = fields.Str(required=False)
    
    version = fields.Str(required=False)
    

