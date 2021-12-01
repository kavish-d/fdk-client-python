"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class OrderDiscountRequest(BaseSchema):

    
    currency = fields.Str(required=False)
    
    order_amount = fields.Float(required=False)
    

