"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema
































class BulkInventoryGetItems(BaseSchema):
    # Catalog swagger.json

    
    created_by = fields.Dict(required=False)
    
    created_on = fields.Str(required=False)
    
    succeed = fields.Int(required=False)
    
    failed = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    total = fields.Int(required=False)
    
    modified_by = fields.Dict(required=False)
    
    cancelled = fields.Int(required=False)
    
    file_path = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    stage = fields.Str(required=False)
    
    failed_records = fields.List(fields.Str(required=False), required=False)
    
    cancelled_records = fields.List(fields.Str(required=False), required=False)
    
    id = fields.Str(required=False)
    

