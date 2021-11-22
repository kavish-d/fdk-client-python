"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *





from .ProductPriceInfo import ProductPriceInfo





from .CartProduct import CartProduct

from .PromoMeta import PromoMeta

from .CartProductIdentifer import CartProductIdentifer





from .ProductArticle import ProductArticle



from .ProductAvailability import ProductAvailability

from .ProductPriceInfo import ProductPriceInfo


class CartProductInfo(Schema):

    
    quantity = fields.Int(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    is_set = fields.Boolean(required=False)
    
    key = fields.Str(required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    discount = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    coupon_message = fields.Str(required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    

