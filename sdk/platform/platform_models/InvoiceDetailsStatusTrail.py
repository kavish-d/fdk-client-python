"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *








class InvoiceDetailsStatusTrail(Schema):

    
    _id = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    timestamp = fields.Str(required=False)
    

