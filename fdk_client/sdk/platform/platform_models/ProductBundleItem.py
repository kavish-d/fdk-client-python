"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema














class ProductBundleItem(BaseSchema):
    # Catalog swagger.json

    
    allow_remove = fields.Boolean(required=False)
    
    auto_add_to_cart = fields.Boolean(required=False)
    
    product_uid = fields.Int(required=False)
    
    auto_select = fields.Boolean(required=False)
    
    max_quantity = fields.Int(required=False)
    
    min_quantity = fields.Int(required=False)
    

