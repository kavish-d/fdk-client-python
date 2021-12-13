"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .RootPaymentMode import RootPaymentMode

from .PaymentFlow import PaymentFlow


class PaymentOptionAndFlow(BaseSchema):

    
    payment_option = fields.List(fields.Nested(RootPaymentMode, required=False), required=False)
    
    payment_flows = fields.Nested(PaymentFlow, required=False)
    

