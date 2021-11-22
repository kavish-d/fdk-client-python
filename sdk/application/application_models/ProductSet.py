"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *



from .ProductSetDistribution import ProductSetDistribution


class ProductSet(Schema):

    
    quantity = fields.Int(required=False)
    
    size_distribution = fields.Nested(ProductSetDistribution, required=False)
    

