"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema


















class DetailedPlanComponents(BaseSchema):

    
    name = fields.Str(required=False)
    
    slug = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    group = fields.Str(required=False)
    
    icon = fields.Str(required=False)
    
    links = fields.Dict(required=False)
    
    enabled = fields.Boolean(required=False)
    
    display_text = fields.Str(required=False)
    
