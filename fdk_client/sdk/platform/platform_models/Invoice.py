"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .InvoiceDetails import InvoiceDetails

from .InvoiceItems import InvoiceItems


class Invoice(BaseSchema):
    # Billing swagger.json

    
    invoice = fields.Nested(InvoiceDetails, required=False)
    
    invoice_items = fields.List(fields.Nested(InvoiceItems, required=False), required=False)
    

