"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .TotalLineItemsPriceSetShopMoney import TotalLineItemsPriceSetShopMoney

from .TotalLineItemsPriceSetPresentmentMoney import TotalLineItemsPriceSetPresentmentMoney


class TotalLineItemsPriceSet(Schema):

    
    shop_money = fields.Nested(TotalLineItemsPriceSetShopMoney, required=False)
    
    presentment_money = fields.Nested(TotalLineItemsPriceSetPresentmentMoney, required=False)
    

