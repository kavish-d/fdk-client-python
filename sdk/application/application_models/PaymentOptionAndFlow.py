"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .RootPaymentMode import RootPaymentMode

from .PaymentFlow import PaymentFlow


class PaymentOptionAndFlow(Schema):

    
    payment_option = fields.List(fields.Nested(RootPaymentMode, required=False), required=False)
    
    payment_flows = fields.Nested(PaymentFlow, required=False)
    

