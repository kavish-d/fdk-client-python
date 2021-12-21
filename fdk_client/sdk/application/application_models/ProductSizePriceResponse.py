"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .MarketPlaceSttributes import MarketPlaceSttributes









from .ProductSet import ProductSet

from .ProductStockPrice import ProductStockPrice

from .ArticleAssignment import ArticleAssignment

from .ProductStockPrice import ProductStockPrice

from .ReturnConfig import ReturnConfig



from .Store import Store





from .StrategyWiseListing import StrategyWiseListing



from .Seller import Seller


class ProductSizePriceResponse(BaseSchema):
    # Catalog swagger.json

    
    marketplace_attributes = fields.List(fields.Nested(MarketPlaceSttributes, required=False), required=False)
    
    quantity = fields.Int(required=False)
    
    long_lat = fields.List(fields.Float(required=False), required=False)
    
    article_id = fields.Str(required=False)
    
    discount = fields.Str(required=False)
    
    set = fields.Nested(ProductSet, required=False)
    
    price_per_piece = fields.Nested(ProductStockPrice, required=False)
    
    article_assignment = fields.Nested(ArticleAssignment, required=False)
    
    price = fields.Nested(ProductStockPrice, required=False)
    
    return_config = fields.Nested(ReturnConfig, required=False)
    
    item_type = fields.Str(required=False)
    
    store = fields.Nested(Store, required=False)
    
    pincode = fields.Int(required=False)
    
    seller_count = fields.Int(required=False)
    
    strategy_wise_listing = fields.List(fields.Nested(StrategyWiseListing, required=False), required=False)
    
    special_badge = fields.Str(required=False)
    
    seller = fields.Nested(Seller, required=False)
    

