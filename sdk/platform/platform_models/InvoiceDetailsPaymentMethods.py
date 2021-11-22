"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *







from .InvoiceDetailsPaymentMethodsData import InvoiceDetailsPaymentMethodsData




class InvoiceDetailsPaymentMethods(Schema):

    
    id = fields.Int(required=False)
    
    type = fields.Str(required=False)
    
    pg_payment_method_id = fields.Str(required=False)
    
    data = fields.Nested(InvoiceDetailsPaymentMethodsData, required=False)
    
    is_default = fields.Boolean(required=False)
    

