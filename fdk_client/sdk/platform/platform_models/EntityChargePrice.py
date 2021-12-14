"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class EntityChargePrice(BaseSchema):
    # Billing swagger.json

    
    amount = fields.Float(required=False)
    
    currency_code = fields.Str(required=False)
    

