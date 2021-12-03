"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema














class CatalogInsightBrand(BaseSchema):

    
    name = fields.Str(required=False)
    
    total_articles = fields.Int(required=False)
    
    total_sizes = fields.Int(required=False)
    
    available_sizes = fields.Int(required=False)
    
    available_articles = fields.Int(required=False)
    
    article_freshness = fields.Int(required=False)
    

