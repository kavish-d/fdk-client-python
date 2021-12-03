"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema












class ReviewFacet(BaseSchema):

    
    display = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    selected = fields.Boolean(required=False)
    
    slug = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
