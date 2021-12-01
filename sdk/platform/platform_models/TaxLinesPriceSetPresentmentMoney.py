"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class TaxLinesPriceSetPresentmentMoney(BaseSchema):

    
    currency_code = fields.Str(required=False)
    
    amount = fields.Str(required=False)
    

