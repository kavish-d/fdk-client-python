"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class CrossSellingData(BaseSchema):

    
    articles = fields.Int(required=False)
    
    products = fields.Int(required=False)
    

