"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class PaymentConfirmationMode(BaseSchema):
    # Payment swagger.json

    
    amount = fields.Float(required=False)
    
    mode = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    name = fields.Str(required=False)
    

