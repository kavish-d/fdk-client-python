"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .RootPaymentMode import RootPaymentMode


class PaymentOptions(Schema):

    
    payment_option = fields.List(fields.Nested(RootPaymentMode, required=False), required=False)
    

