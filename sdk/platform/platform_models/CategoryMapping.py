"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .CategoryMappingValues import CategoryMappingValues

from .CategoryMappingValues import CategoryMappingValues

from .CategoryMappingValues import CategoryMappingValues


class CategoryMapping(BaseSchema):

    
    facebook = fields.Nested(CategoryMappingValues, required=False)
    
    ajio = fields.Nested(CategoryMappingValues, required=False)
    
    google = fields.Nested(CategoryMappingValues, required=False)
    

