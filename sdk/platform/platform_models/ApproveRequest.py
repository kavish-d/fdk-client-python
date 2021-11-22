"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *










class ApproveRequest(Schema):

    
    approve = fields.Boolean(required=False)
    
    entity_type = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    reason = fields.Str(required=False)
    

