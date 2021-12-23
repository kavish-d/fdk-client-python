"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema









from .Seller import Seller

from .ProductSet import ProductSet



from .Store import Store

from .ProductStockPrice import ProductStockPrice

from .StrategyWiseListing import StrategyWiseListing

from .ArticleAssignment import ArticleAssignment



from .MarketPlaceSttributes import MarketPlaceSttributes





from .ProductStockPrice import ProductStockPrice

from .ReturnConfig import ReturnConfig


class ProductSizePriceResponse(BaseSchema):
    # Catalog swagger.json

    
    seller_count = fields.Int(required=False)
    
    discount = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    
    seller = fields.Nested(Seller, required=False)
    
    set = fields.Nested(ProductSet, required=False)
    
    article_id = fields.Str(required=False)
    
    store = fields.Nested(Store, required=False)
    
    price = fields.Nested(ProductStockPrice, required=False)
    
    strategy_wise_listing = fields.List(fields.Nested(StrategyWiseListing, required=False), required=False)
    
    article_assignment = fields.Nested(ArticleAssignment, required=False)
    
    item_type = fields.Str(required=False)
    
    marketplace_attributes = fields.List(fields.Nested(MarketPlaceSttributes, required=False), required=False)
    
    long_lat = fields.List(fields.Float(required=False), required=False)
    
    special_badge = fields.Str(required=False)
    
    price_per_piece = fields.Nested(ProductStockPrice, required=False)
    
    return_config = fields.Nested(ReturnConfig, required=False)
    

