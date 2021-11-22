"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
















class FileJobResponse(Schema):

    
    stage = fields.Str(required=False)
    
    total = fields.Int(required=False)
    
    failed = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    body = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    file_type = fields.Str(required=False)
    

