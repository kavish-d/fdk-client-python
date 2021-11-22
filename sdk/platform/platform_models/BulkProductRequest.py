"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *










class BulkProductRequest(Schema):

    
    template_tag = fields.Str(required=False)
    
    batch_id = fields.Str(required=False)
    
    data = fields.List(fields.Dict(required=False), required=False)
    
    company_id = fields.Int(required=False)
    

