"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class CatalogInsightItem(BaseSchema):

    
    sellable_count = fields.Int(required=False)
    
    count = fields.Int(required=False)
    
    out_of_stock_count = fields.Int(required=False)
    

