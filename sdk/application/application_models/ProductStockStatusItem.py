"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *



from .ProductStockPrice import ProductStockPrice

from .StoreDetail import StoreDetail

from .CompanyDetail import CompanyDetail





from .Seller import Seller






class ProductStockStatusItem(Schema):

    
    quantity = fields.Int(required=False)
    
    price = fields.Nested(ProductStockPrice, required=False)
    
    store = fields.Nested(StoreDetail, required=False)
    
    company = fields.Nested(CompanyDetail, required=False)
    
    item_id = fields.Int(required=False)
    
    identifier = fields.Dict(required=False)
    
    seller = fields.Nested(Seller, required=False)
    
    size = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    

