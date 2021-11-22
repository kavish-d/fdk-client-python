"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class InvoiceItemsPlanRecurring(Schema):

    
    interval = fields.Str(required=False)
    
    interval_count = fields.Int(required=False)
    

