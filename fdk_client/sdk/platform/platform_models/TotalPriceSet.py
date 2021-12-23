"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .TotalPriceSetShopMoney import TotalPriceSetShopMoney

from .TotalPriceSetPresentmentMoney import TotalPriceSetPresentmentMoney


class TotalPriceSet(BaseSchema):
    # Order swagger.json

    
    shop_money = fields.Nested(TotalPriceSetShopMoney, required=False)
    
    presentment_money = fields.Nested(TotalPriceSetPresentmentMoney, required=False)
    

