"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema



from .UserDetail import UserDetail

from .ProductTemplate import ProductTemplate











from .UserDetail import UserDetail
















class ProductBulkRequest(BaseSchema):

    
    succeed = fields.Int(required=False)
    
    created_by = fields.Nested(UserDetail, required=False)
    
    template = fields.Nested(ProductTemplate, required=False)
    
    template_tag = fields.Str(required=False)
    
    file_path = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    failed_records = fields.List(fields.Str(required=False), required=False)
    
    cancelled = fields.Int(required=False)
    
    modified_by = fields.Nested(UserDetail, required=False)
    
    cancelled_records = fields.List(fields.Str(required=False), required=False)
    
    created_on = fields.Str(required=False)
    
    total = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    failed = fields.Int(required=False)
    
    stage = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    

