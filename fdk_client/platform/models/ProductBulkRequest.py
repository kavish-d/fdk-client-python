"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema







from .ProductTemplate import ProductTemplate













from .UserDetail import UserDetail



from .UserDetail import UserDetail








class ProductBulkRequest(BaseSchema):
    # Catalog swagger.json

    
    total = fields.Int(required=False)
    
    cancelled = fields.Int(required=False)
    
    template_tag = fields.Str(required=False)
    
    template = fields.Nested(ProductTemplate, required=False)
    
    failed_records = fields.List(fields.Str(required=False), required=False)
    
    stage = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    file_path = fields.Str(required=False)
    
    cancelled_records = fields.List(fields.Str(required=False), required=False)
    
    created_by = fields.Nested(UserDetail, required=False)
    
    company_id = fields.Int(required=False)
    
    modified_by = fields.Nested(UserDetail, required=False)
    
    failed = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    succeed = fields.Int(required=False)
    

