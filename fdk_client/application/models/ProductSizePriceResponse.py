"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .StrategyWiseListing import StrategyWiseListing





from .MarketPlaceSttributes import MarketPlaceSttributes





from .Seller import Seller

from .Store import Store





from .ReturnConfig import ReturnConfig

from .ProductStockPrice import ProductStockPrice

from .ProductStockPrice import ProductStockPrice

from .ProductSet import ProductSet

from .ArticleAssignment import ArticleAssignment






class ProductSizePriceResponse(BaseSchema):
    # Catalog swagger.json

    
    strategy_wise_listing = fields.List(fields.Nested(StrategyWiseListing, required=False), required=False)
    
    long_lat = fields.List(fields.Float(required=False), required=False)
    
    item_type = fields.Str(required=False)
    
    marketplace_attributes = fields.List(fields.Nested(MarketPlaceSttributes, required=False), required=False)
    
    seller_count = fields.Int(required=False)
    
    discount = fields.Str(required=False)
    
    seller = fields.Nested(Seller, required=False)
    
    store = fields.Nested(Store, required=False)
    
    pincode = fields.Int(required=False)
    
    article_id = fields.Str(required=False)
    
    return_config = fields.Nested(ReturnConfig, required=False)
    
    price_per_piece = fields.Nested(ProductStockPrice, required=False)
    
    price = fields.Nested(ProductStockPrice, required=False)
    
    set = fields.Nested(ProductSet, required=False)
    
    article_assignment = fields.Nested(ArticleAssignment, required=False)
    
    special_badge = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    

