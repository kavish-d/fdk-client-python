"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .PaymentFlow import PaymentFlow

from .RootPaymentMode import RootPaymentMode


class PaymentOptionAndFlow(BaseSchema):

    
    payment_flows = fields.Nested(PaymentFlow, required=False)
    
    payment_option = fields.List(fields.Nested(RootPaymentMode, required=False), required=False)
    

