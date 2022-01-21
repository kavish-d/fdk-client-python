"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .ProductAvailability import ProductAvailability



from .CartProductIdentifer import CartProductIdentifer





from .ProductPriceInfo import ProductPriceInfo

from .CartProduct import CartProduct



from .PromoMeta import PromoMeta





from .ProductPriceInfo import ProductPriceInfo

from .ProductArticle import ProductArticle


class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    quantity = fields.Int(required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    key = fields.Str(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    discount = fields.Str(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    message = fields.Str(required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    coupon_message = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    

