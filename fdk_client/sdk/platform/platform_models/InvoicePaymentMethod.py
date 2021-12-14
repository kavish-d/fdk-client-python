"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema




class InvoicePaymentMethod(BaseSchema):
    # Billing swagger.json

    
    pg_payment_method_id = fields.Str(required=False)
    

