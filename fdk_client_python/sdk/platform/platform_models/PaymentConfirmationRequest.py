"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .MultiTenderPaymentMethod import MultiTenderPaymentMethod




class PaymentConfirmationRequest(BaseSchema):

    
    payment_methods = fields.List(fields.Nested(MultiTenderPaymentMethod, required=False), required=False)
    
    order_id = fields.Str(required=False)
    

