"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *














class CompanyConfig(Schema):

    
    company_id = fields.Int(required=False)
    
    exclude_steps = fields.List(fields.Int(required=False), required=False)
    
    hidden_closet_keys = fields.List(fields.Str(required=False), required=False)
    
    open_tags = fields.Dict(required=False)
    
    tax_identifiers = fields.List(fields.Str(required=False), required=False)
    
    delete_quantity_threshold = fields.Int(required=False)
    

