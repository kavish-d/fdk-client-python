"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .ProductArticle import ProductArticle







from .ProductPriceInfo import ProductPriceInfo



from .CartProductIdentifer import CartProductIdentifer

from .ProductAvailability import ProductAvailability

from .ProductPriceInfo import ProductPriceInfo

from .PromoMeta import PromoMeta







from .CartProduct import CartProduct


class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    article = fields.Nested(ProductArticle, required=False)
    
    discount = fields.Str(required=False)
    
    key = fields.Str(required=False)
    
    coupon_message = fields.Str(required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    is_set = fields.Boolean(required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    quantity = fields.Int(required=False)
    
    message = fields.Str(required=False)
    
    product = fields.Nested(CartProduct, required=False)
    

