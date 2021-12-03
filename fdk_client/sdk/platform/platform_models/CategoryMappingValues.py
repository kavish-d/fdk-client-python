"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class CategoryMappingValues(BaseSchema):

    
    catalog_id = fields.Int(required=False)
    
    name = fields.Str(required=False)
    
