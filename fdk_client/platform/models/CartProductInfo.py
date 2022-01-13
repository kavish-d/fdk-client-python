"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .PromoMeta import PromoMeta

from .ProductArticle import ProductArticle







from .CartProductIdentifer import CartProductIdentifer

from .ProductPriceInfo import ProductPriceInfo

from .ProductPriceInfo import ProductPriceInfo









from .CartProduct import CartProduct

from .ProductAvailability import ProductAvailability


class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    message = fields.Str(required=False)
    
    discount = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    coupon_message = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    

