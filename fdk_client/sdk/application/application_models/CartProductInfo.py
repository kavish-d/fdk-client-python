"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema







from .ProductPriceInfo import ProductPriceInfo

from .CartProductIdentifer import CartProductIdentifer



from .PromoMeta import PromoMeta

from .ProductArticle import ProductArticle



from .CartProduct import CartProduct



from .ProductAvailability import ProductAvailability

from .ProductPriceInfo import ProductPriceInfo




class CartProductInfo(BaseSchema):
    # Cart swagger.json

    
    key = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    
    bulk_offer = fields.Dict(required=False)
    
    price = fields.Nested(ProductPriceInfo, required=False)
    
    identifiers = fields.Nested(CartProductIdentifer, required=False)
    
    discount = fields.Str(required=False)
    
    promo_meta = fields.Nested(PromoMeta, required=False)
    
    article = fields.Nested(ProductArticle, required=False)
    
    message = fields.Str(required=False)
    
    product = fields.Nested(CartProduct, required=False)
    
    coupon_message = fields.Str(required=False)
    
    availability = fields.Nested(ProductAvailability, required=False)
    
    price_per_unit = fields.Nested(ProductPriceInfo, required=False)
    
    quantity = fields.Int(required=False)
    

