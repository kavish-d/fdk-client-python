"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .TaxLinesPriceSetShopMoney import TaxLinesPriceSetShopMoney

from .TaxLinesPriceSetPresentmentMoney import TaxLinesPriceSetPresentmentMoney


class TaxLinesPriceSet(BaseSchema):

    
    shop_money = fields.Nested(TaxLinesPriceSetShopMoney, required=False)
    
    presentment_money = fields.Nested(TaxLinesPriceSetPresentmentMoney, required=False)
    

