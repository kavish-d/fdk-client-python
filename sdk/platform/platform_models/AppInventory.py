"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .InventoryBrandRule import InventoryBrandRule

from .InventoryStoreRule import InventoryStoreRule







from .InventoryPaymentConfig import InventoryPaymentConfig

from .InventoryArticleAssignment import InventoryArticleAssignment


class AppInventory(Schema):

    
    brand = fields.Nested(InventoryBrandRule, required=False)
    
    store = fields.Nested(InventoryStoreRule, required=False)
    
    image = fields.List(fields.Str(required=False), required=False)
    
    franchise_enabled = fields.Boolean(required=False)
    
    out_of_stock = fields.Boolean(required=False)
    
    payment = fields.Nested(InventoryPaymentConfig, required=False)
    
    article_assignment = fields.Nested(InventoryArticleAssignment, required=False)
    

