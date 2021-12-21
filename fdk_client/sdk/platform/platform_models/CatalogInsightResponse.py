"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .CatalogInsightBrand import CatalogInsightBrand

from .CatalogInsightItem import CatalogInsightItem


class CatalogInsightResponse(BaseSchema):
    # Catalog swagger.json

    
    brand_distribution = fields.Nested(CatalogInsightBrand, required=False)
    
    item = fields.Nested(CatalogInsightItem, required=False)
    

