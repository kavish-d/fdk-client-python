"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *







from .StagesFilters import StagesFilters


class Stages(Schema):

    
    text = fields.Str(required=False)
    
    value = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    
    filters = fields.Nested(StagesFilters, required=False)
    

