"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .PresentmentMoney import PresentmentMoney

from .ShopMoney import ShopMoney


class TotalDiscountsSet(BaseSchema):

    
    presentment_money = fields.Nested(PresentmentMoney, required=False)
    
    shop_money = fields.Nested(ShopMoney, required=False)
    

