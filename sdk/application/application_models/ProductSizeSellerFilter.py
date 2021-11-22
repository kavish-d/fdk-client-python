"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *








class ProductSizeSellerFilter(Schema):

    
    value = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    is_selected = fields.Boolean(required=False)
    

