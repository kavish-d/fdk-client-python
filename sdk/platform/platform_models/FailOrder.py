"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *







from .MarketplaceOrder import MarketplaceOrder












class FailOrder(Schema):

    
    updated_at = fields.Str(required=False)
    
    _id = fields.Str(required=False)
    
    reason = fields.Str(required=False)
    
    marketplace_order = fields.Nested(MarketplaceOrder, required=False)
    
    marketplace_order_id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    marketplace = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    

