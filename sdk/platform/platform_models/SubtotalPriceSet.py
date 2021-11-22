"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .SubtotalPriceSetShopMoney import SubtotalPriceSetShopMoney

from .SubtotalPriceSetPresentmentMoney import SubtotalPriceSetPresentmentMoney


class SubtotalPriceSet(Schema):

    
    shop_money = fields.Nested(SubtotalPriceSetShopMoney, required=False)
    
    presentment_money = fields.Nested(SubtotalPriceSetPresentmentMoney, required=False)
    

