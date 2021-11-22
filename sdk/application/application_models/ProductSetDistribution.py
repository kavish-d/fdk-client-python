"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .ProductSetDistributionSize import ProductSetDistributionSize


class ProductSetDistribution(Schema):

    
    sizes = fields.List(fields.Nested(ProductSetDistributionSize, required=False), required=False)
    

