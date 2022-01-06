"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductSet import ProductSet

from .Store import Store

from .ReturnConfig import ReturnConfig

from .ProductStockPrice import ProductStockPrice





from .ProductStockPrice import ProductStockPrice

from .MarketPlaceSttributes import MarketPlaceSttributes



from .ArticleAssignment import ArticleAssignment







from .Seller import Seller



from .StrategyWiseListing import StrategyWiseListing




class ProductSizePriceResponse(BaseSchema):
    # Catalog swagger.json

    
    set = fields.Nested(ProductSet, required=False)
    
    store = fields.Nested(Store, required=False)
    
    return_config = fields.Nested(ReturnConfig, required=False)
    
    price_per_piece = fields.Nested(ProductStockPrice, required=False)
    
    item_type = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    price = fields.Nested(ProductStockPrice, required=False)
    
    marketplace_attributes = fields.List(fields.Nested(MarketPlaceSttributes, required=False), required=False)
    
    discount = fields.Str(required=False)
    
    article_assignment = fields.Nested(ArticleAssignment, required=False)
    
    long_lat = fields.List(fields.Float(required=False), required=False)
    
    article_id = fields.Str(required=False)
    
    seller_count = fields.Int(required=False)
    
    seller = fields.Nested(Seller, required=False)
    
    special_badge = fields.Str(required=False)
    
    strategy_wise_listing = fields.List(fields.Nested(StrategyWiseListing, required=False), required=False)
    
    pincode = fields.Int(required=False)
    

