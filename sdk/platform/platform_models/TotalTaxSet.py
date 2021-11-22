"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .TotalTaxSetShopMoney import TotalTaxSetShopMoney

from .TotalTaxSetPresentmentMoney import TotalTaxSetPresentmentMoney


class TotalTaxSet(Schema):

    
    shop_money = fields.Nested(TotalTaxSetShopMoney, required=False)
    
    presentment_money = fields.Nested(TotalTaxSetPresentmentMoney, required=False)
    

