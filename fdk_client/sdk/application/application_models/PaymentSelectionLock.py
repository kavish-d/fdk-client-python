"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema








class PaymentSelectionLock(BaseSchema):

    
    default_options = fields.Str(required=False)
    
    enabled = fields.Boolean(required=False)
    
    payment_identifier = fields.Str(required=False)
    

