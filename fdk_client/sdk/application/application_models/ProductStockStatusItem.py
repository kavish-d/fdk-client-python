"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema





from .CompanyDetail import CompanyDetail



from .ProductStockPrice import ProductStockPrice

from .StoreDetail import StoreDetail



from .Seller import Seller




class ProductStockStatusItem(BaseSchema):
    # Catalog swagger.json

    
    uid = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    company = fields.Nested(CompanyDetail, required=False)
    
    item_id = fields.Int(required=False)
    
    price = fields.Nested(ProductStockPrice, required=False)
    
    store = fields.Nested(StoreDetail, required=False)
    
    size = fields.Str(required=False)
    
    seller = fields.Nested(Seller, required=False)
    
    identifier = fields.Dict(required=False)
    

