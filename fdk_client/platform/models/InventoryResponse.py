"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema




























class InventoryResponse(BaseSchema):
    # Catalog swagger.json

    
    identifiers = fields.Dict(required=False)
    
    price_effective = fields.Int(required=False)
    
    uid = fields.Str(required=False)
    
    seller_identifier = fields.Int(required=False)
    
    price = fields.Int(required=False)
    
    item_id = fields.Int(required=False)
    
    currency = fields.Str(required=False)
    
    size = fields.Str(required=False)
    
    sellable_quantity = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    
    inventory_updated_on = fields.Str(required=False)
    
    store = fields.Dict(required=False)
    
    price_transfer = fields.Int(required=False)
    

