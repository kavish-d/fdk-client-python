"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class InvoiceDetailsPaymentMethodsDataThreeDSecureUsage(Schema):

    
    supported = fields.Boolean(required=False)
    

