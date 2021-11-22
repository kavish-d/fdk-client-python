"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class InventoryPaymentConfig(Schema):

    
    mode_of_payment = fields.Str(required=False)
    
    source = fields.Str(required=False)
    

