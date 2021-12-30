"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Seller import Seller

from .ReturnConfig import ReturnConfig

from .ArticleAssignment import ArticleAssignment

from .ProductStockPrice import ProductStockPrice

from .MarketPlaceSttributes import MarketPlaceSttributes





from .Store import Store







from .ProductSet import ProductSet



from .StrategyWiseListing import StrategyWiseListing

from .ProductStockPrice import ProductStockPrice






class ProductSizePriceResponse(BaseSchema):
    # Catalog swagger.json

    
    seller = fields.Nested(Seller, required=False)
    
    return_config = fields.Nested(ReturnConfig, required=False)
    
    article_assignment = fields.Nested(ArticleAssignment, required=False)
    
    price = fields.Nested(ProductStockPrice, required=False)
    
    marketplace_attributes = fields.List(fields.Nested(MarketPlaceSttributes, required=False), required=False)
    
    article_id = fields.Str(required=False)
    
    item_type = fields.Str(required=False)
    
    store = fields.Nested(Store, required=False)
    
    quantity = fields.Int(required=False)
    
    long_lat = fields.List(fields.Float(required=False), required=False)
    
    seller_count = fields.Int(required=False)
    
    set = fields.Nested(ProductSet, required=False)
    
    special_badge = fields.Str(required=False)
    
    strategy_wise_listing = fields.List(fields.Nested(StrategyWiseListing, required=False), required=False)
    
    price_per_piece = fields.Nested(ProductStockPrice, required=False)
    
    discount = fields.Str(required=False)
    
    pincode = fields.Int(required=False)
    

