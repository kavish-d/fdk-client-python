"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class PaymentModeLogo(BaseSchema):

    
    large = fields.Str(required=False)
    
    small = fields.Str(required=False)
    

