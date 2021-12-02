"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .PaymentOptions import PaymentOptions




class PaymentOptionsResponse(BaseSchema):

    
    payment_options = fields.Nested(PaymentOptions, required=False)
    
    success = fields.Boolean(required=False)
    

