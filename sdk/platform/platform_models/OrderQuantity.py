"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *








class OrderQuantity(Schema):

    
    is_set = fields.Boolean(required=False)
    
    maximum = fields.Int(required=False)
    
    minimum = fields.Int(required=False)
    

