"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema

from .Hierarchy import Hierarchy





from .CategoryMapping import CategoryMapping

















from .Media2 import Media2










class Category(BaseSchema):
    # Catalog swagger.json

    
    hierarchy = fields.List(fields.Nested(Hierarchy, required=False), required=False)
    
    uid = fields.Int(required=False)
    
    departments = fields.List(fields.Int(required=False), required=False)
    
    marketplaces = fields.Nested(CategoryMapping, required=False)
    
    modified_by = fields.Dict(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    level = fields.Int(required=False)
    
    priority = fields.Int(required=False)
    
    is_active = fields.Boolean(required=False)
    
    media = fields.Nested(Media2, required=False)
    
    _id = fields.Str(required=False)
    
    tryouts = fields.List(fields.Str(required=False), required=False)
    
    created_by = fields.Dict(required=False)
    
    synonyms = fields.List(fields.Str(required=False), required=False)
    

