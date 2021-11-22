"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class SubtotalPriceSetPresentmentMoney(Schema):

    
    amount = fields.Str(required=False)
    
    currency_code = fields.Str(required=False)
    

