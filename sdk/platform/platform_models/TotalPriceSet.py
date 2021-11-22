"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .TotalPriceSetShopMoney import TotalPriceSetShopMoney

from .TotalPriceSetPresentmentMoney import TotalPriceSetPresentmentMoney


class TotalPriceSet(Schema):

    
    shop_money = fields.Nested(TotalPriceSetShopMoney, required=False)
    
    presentment_money = fields.Nested(TotalPriceSetPresentmentMoney, required=False)
    

