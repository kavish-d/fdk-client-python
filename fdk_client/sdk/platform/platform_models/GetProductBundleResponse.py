"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema









from .GetProducts import GetProducts












class GetProductBundleResponse(BaseSchema):

    
    name = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    slug = fields.Str(required=False)
    
    is_active = fields.Boolean(required=False)
    
    products = fields.List(fields.Nested(GetProducts, required=False), required=False)
    
    company_id = fields.Int(required=False)
    
    logo = fields.Str(required=False)
    
    same_store_assignment = fields.Boolean(required=False)
    
    choice = fields.Str(required=False)
    
    page_visibility = fields.List(fields.Str(required=False), required=False)
    
