"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .CatalogInsightBrand import CatalogInsightBrand

from .CrossSellingData import CrossSellingData


class CrossSellingResponse(Schema):

    
    brand_distribution = fields.Nested(CatalogInsightBrand, required=False)
    
    data = fields.Nested(CrossSellingData, required=False)
    

