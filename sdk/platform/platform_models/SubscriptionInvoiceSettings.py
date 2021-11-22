"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class SubscriptionInvoiceSettings(Schema):

    
    generation = fields.Boolean(required=False)
    
    charging = fields.Boolean(required=False)
    

