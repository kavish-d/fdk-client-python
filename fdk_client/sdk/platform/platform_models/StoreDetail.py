"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema
























class StoreDetail(BaseSchema):

    
    name = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    store_code = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    created_on = fields.Str(required=False)
    
    timing = fields.Dict(required=False)
    
    additional_contacts = fields.List(fields.Dict(required=False), required=False)
    
    uid = fields.Int(required=False)
    
    store_type = fields.Str(required=False)
    
    documents = fields.List(fields.Dict(required=False), required=False)
    
    display_name = fields.Str(required=False)
    
