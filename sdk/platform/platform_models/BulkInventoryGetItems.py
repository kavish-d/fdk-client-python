"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema
































class BulkInventoryGetItems(BaseSchema):

    
    created_on = fields.Str(required=False)
    
    file_path = fields.Str(required=False)
    
    cancelled = fields.Int(required=False)
    
    company_id = fields.Int(required=False)
    
    modified_by = fields.Dict(required=False)
    
    stage = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    failed_records = fields.List(fields.Str(required=False), required=False)
    
    cancelled_records = fields.List(fields.Str(required=False), required=False)
    
    created_by = fields.Dict(required=False)
    
    failed = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    total = fields.Int(required=False)
    
    succeed = fields.Int(required=False)
    

