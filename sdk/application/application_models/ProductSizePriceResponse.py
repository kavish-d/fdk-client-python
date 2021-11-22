"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *



from .MarketPlaceSttributes import MarketPlaceSttributes

from .ProductSet import ProductSet





from .ProductStockPrice import ProductStockPrice

from .ProductStockPrice import ProductStockPrice



from .Store import Store

from .ArticleAssignment import ArticleAssignment





from .ReturnConfig import ReturnConfig



from .Seller import Seller



from .StrategyWiseListing import StrategyWiseListing


class ProductSizePriceResponse(Schema):

    
    quantity = fields.Int(required=False)
    
    marketplace_attributes = fields.List(fields.Nested(MarketPlaceSttributes, required=False), required=False)
    
    set = fields.Nested(ProductSet, required=False)
    
    long_lat = fields.List(fields.Float(required=False), required=False)
    
    pincode = fields.Int(required=False)
    
    price = fields.Nested(ProductStockPrice, required=False)
    
    price_per_piece = fields.Nested(ProductStockPrice, required=False)
    
    discount = fields.Str(required=False)
    
    store = fields.Nested(Store, required=False)
    
    article_assignment = fields.Nested(ArticleAssignment, required=False)
    
    seller_count = fields.Int(required=False)
    
    item_type = fields.Str(required=False)
    
    return_config = fields.Nested(ReturnConfig, required=False)
    
    article_id = fields.Str(required=False)
    
    seller = fields.Nested(Seller, required=False)
    
    special_badge = fields.Str(required=False)
    
    strategy_wise_listing = fields.List(fields.Nested(StrategyWiseListing, required=False), required=False)
    

