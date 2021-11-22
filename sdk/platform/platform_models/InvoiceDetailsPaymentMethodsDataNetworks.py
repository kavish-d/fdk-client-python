"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class InvoiceDetailsPaymentMethodsDataNetworks(Schema):

    
    available = fields.List(fields.Str(required=False), required=False)
    
    preferred = fields.Str(required=False)
    

