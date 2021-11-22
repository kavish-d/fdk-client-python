"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .InvoiceCredSerializer import InvoiceCredSerializer

from .InvoiceCredSerializer import InvoiceCredSerializer


class InvoiceDetailsSerializer(Schema):

    
    e_waybill = fields.Nested(InvoiceCredSerializer, required=False)
    
    e_invoice = fields.Nested(InvoiceCredSerializer, required=False)
    

