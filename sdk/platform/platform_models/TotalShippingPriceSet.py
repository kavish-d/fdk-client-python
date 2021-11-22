"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .TotalShippingPriceSetShopMoney import TotalShippingPriceSetShopMoney

from .TotalShippingPriceSetPresentmentMoney import TotalShippingPriceSetPresentmentMoney


class TotalShippingPriceSet(Schema):

    
    shop_money = fields.Nested(TotalShippingPriceSetShopMoney, required=False)
    
    presentment_money = fields.Nested(TotalShippingPriceSetPresentmentMoney, required=False)
    

