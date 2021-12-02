"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema



from .PaymentOptionAndFlow import PaymentOptionAndFlow


class PaymentModeRouteResponse(BaseSchema):

    
    success = fields.Boolean(required=False)
    
    payment_options = fields.Nested(PaymentOptionAndFlow, required=False)
    

