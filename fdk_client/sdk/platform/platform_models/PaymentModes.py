"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .PaymentAllowValue import PaymentAllowValue








class PaymentModes(BaseSchema):
    # Cart swagger.json

    
    uses = fields.Nested(PaymentAllowValue, required=False)
    
    networks = fields.List(fields.Str(required=False), required=False)
    
    codes = fields.List(fields.Str(required=False), required=False)
    
    types = fields.List(fields.Str(required=False), required=False)
    

