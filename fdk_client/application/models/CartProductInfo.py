"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .CartProductIdentifer import CartProductIdentifer



from .PromoMeta import PromoMeta

from .ProductArticle import ProductArticle

from .CartProduct import CartProduct



from .ProductPriceInfo import ProductPriceInfo







from .ProductPriceInfo import ProductPriceInfo



from .ProductAvailability import ProductAvailability


class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    bulk_offer = fields.Dict(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    discount = fields.Str(required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    key = fields.Str(required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    coupon_message = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    quantity = fields.Int(required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    message = fields.Str(required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    

