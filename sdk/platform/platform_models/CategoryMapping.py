"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .CategoryMappingValues import CategoryMappingValues

from .CategoryMappingValues import CategoryMappingValues

from .CategoryMappingValues import CategoryMappingValues


class CategoryMapping(Schema):

    
    facebook = fields.Nested(CategoryMappingValues, required=False)
    
    ajio = fields.Nested(CategoryMappingValues, required=False)
    
    google = fields.Nested(CategoryMappingValues, required=False)
    

