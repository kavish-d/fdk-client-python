"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .RootPaymentMode import RootPaymentMode


class PaymentOptions(BaseSchema):

    
    payment_option = fields.List(fields.Nested(RootPaymentMode, required=False), required=False)
    

