"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *










class InvoiceDetailsClient(Schema):

    
    address_lines = fields.List(fields.Str(required=False), required=False)
    
    name = fields.Str(required=False)
    
    email = fields.Str(required=False)
    
    phone = fields.Str(required=False)
    

