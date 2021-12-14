"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class SubscriptionInvoiceSettings(BaseSchema):
    # Billing swagger.json

    
    generation = fields.Boolean(required=False)
    
    charging = fields.Boolean(required=False)
    

