"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .TaxLinesPriceSetShopMoney import TaxLinesPriceSetShopMoney

from .TaxLinesPriceSetPresentmentMoney import TaxLinesPriceSetPresentmentMoney


class TaxLinesPriceSet(Schema):

    
    shop_money = fields.Nested(TaxLinesPriceSetShopMoney, required=False)
    
    presentment_money = fields.Nested(TaxLinesPriceSetPresentmentMoney, required=False)
    

