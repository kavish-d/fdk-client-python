"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema







from .StagesFilters import StagesFilters


class Stage(BaseSchema):

    
    text = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    
    filters = fields.Nested(StagesFilters, required=False)
    

