"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class TotalLineItemsPriceSetShopMoney(BaseSchema):
    # Order swagger.json

    
    amount = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    

