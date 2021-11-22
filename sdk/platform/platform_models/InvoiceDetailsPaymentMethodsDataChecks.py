"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *








class InvoiceDetailsPaymentMethodsDataChecks(Schema):

    
    cvc_check = fields.Str(required=False)
    
    address_line1_check = fields.Str(required=False)
    
    address_postal_code_check = fields.Str(required=False)
    

