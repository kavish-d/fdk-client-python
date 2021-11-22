"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class TaxLinesPriceSetPresentmentMoney(Schema):

    
    currency_code = fields.Str(required=False)
    
    amount = fields.Str(required=False)
    

