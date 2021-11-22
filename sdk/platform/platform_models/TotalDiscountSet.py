"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .TotalDiscountSetPresentmentMoney import TotalDiscountSetPresentmentMoney

from .TotalDiscountSetShopMoney import TotalDiscountSetShopMoney


class TotalDiscountSet(Schema):

    
    presentment_money = fields.Nested(TotalDiscountSetPresentmentMoney, required=False)
    
    shop_money = fields.Nested(TotalDiscountSetShopMoney, required=False)
    

