"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .PriceSetShopMoney import PriceSetShopMoney

from .PriceSetPresentmentMoney import PriceSetPresentmentMoney


class PriceSet(BaseSchema):
    # Order swagger.json

    
    shop_money = fields.Nested(PriceSetShopMoney, required=False)
    
    presentment_money = fields.Nested(PriceSetPresentmentMoney, required=False)
    

