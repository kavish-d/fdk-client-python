"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *










class UpdateMediaListRequest(Schema):

    
    approve = fields.Boolean(required=False)
    
    archive = fields.Boolean(required=False)
    
    entity_type = fields.Str(required=False)
    
    ids = fields.List(fields.Str(required=False), required=False)
    

