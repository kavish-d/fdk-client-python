"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema



from .ProductStockPrice import ProductStockPrice

from .ProductStockPrice import ProductStockPrice

from .ReturnConfig import ReturnConfig

from .MarketPlaceSttributes import MarketPlaceSttributes

from .ArticleAssignment import ArticleAssignment







from .StrategyWiseListing import StrategyWiseListing

from .Seller import Seller

from .ProductSet import ProductSet









from .Store import Store


class ProductSizePriceResponse(BaseSchema):

    
    article_id = fields.Str(required=False)
    
    price_per_piece = fields.Nested(ProductStockPrice, required=False)
    
    price = fields.Nested(ProductStockPrice, required=False)
    
    return_config = fields.Nested(ReturnConfig, required=False)
    
    marketplace_attributes = fields.List(fields.Nested(MarketPlaceSttributes, required=False), required=False)
    
    article_assignment = fields.Nested(ArticleAssignment, required=False)
    
    pincode = fields.Int(required=False)
    
    discount = fields.Str(required=False)
    
    special_badge = fields.Str(required=False)
    
    strategy_wise_listing = fields.List(fields.Nested(StrategyWiseListing, required=False), required=False)
    
    seller = fields.Nested(Seller, required=False)
    
    set = fields.Nested(ProductSet, required=False)
    
    item_type = fields.Str(required=False)
    
    long_lat = fields.List(fields.Float(required=False), required=False)
    
    quantity = fields.Int(required=False)
    
    seller_count = fields.Int(required=False)
    
    store = fields.Nested(Store, required=False)
    

