"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class InvoicePaymentMethod(Schema):

    
    pg_payment_method_id = fields.Str(required=False)
    

