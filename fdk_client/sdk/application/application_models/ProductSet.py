"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .ProductSetDistribution import ProductSetDistribution




class ProductSet(BaseSchema):

    
    size_distribution = fields.Nested(ProductSetDistribution, required=False)
    
    quantity = fields.Int(required=False)
    

