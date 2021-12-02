"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .InvoiceCredSerializer import InvoiceCredSerializer

from .InvoiceCredSerializer import InvoiceCredSerializer


class InvoiceDetailsSerializer(BaseSchema):

    
    e_waybill = fields.Nested(InvoiceCredSerializer, required=False)
    
    e_invoice = fields.Nested(InvoiceCredSerializer, required=False)
    

