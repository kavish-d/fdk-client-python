"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .CatalogInsightItem import CatalogInsightItem

from .CatalogInsightBrand import CatalogInsightBrand


class CatalogInsightResponse(Schema):

    
    item = fields.Nested(CatalogInsightItem, required=False)
    
    brand_distribution = fields.Nested(CatalogInsightBrand, required=False)
    

