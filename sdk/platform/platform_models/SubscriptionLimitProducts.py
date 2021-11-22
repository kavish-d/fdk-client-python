"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class SubscriptionLimitProducts(Schema):

    
    bulk = fields.Boolean(required=False)
    
    limit = fields.Int(required=False)
    

