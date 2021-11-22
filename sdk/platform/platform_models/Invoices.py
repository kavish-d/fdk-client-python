"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .InvoicesData import InvoicesData












class Invoices(Schema):

    
    data = fields.List(fields.Nested(InvoicesData, required=False), required=False)
    
    start = fields.Int(required=False)
    
    end = fields.Int(required=False)
    
    limit = fields.Int(required=False)
    
    page = fields.Int(required=False)
    
    total = fields.Int(required=False)
    

