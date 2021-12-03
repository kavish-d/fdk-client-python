"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class InventoryPaymentConfig(BaseSchema):

    
    mode_of_payment = fields.Str(required=False)
    
    source = fields.Str(required=False)
    
