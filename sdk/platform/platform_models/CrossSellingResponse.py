"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .CrossSellingData import CrossSellingData

from .CatalogInsightBrand import CatalogInsightBrand


class CrossSellingResponse(BaseSchema):

    
    data = fields.Nested(CrossSellingData, required=False)
    
    brand_distribution = fields.Nested(CatalogInsightBrand, required=False)
    

