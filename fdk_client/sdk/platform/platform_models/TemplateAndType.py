"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class TemplateAndType(BaseSchema):
    # Communication swagger.json

    
    template_type = fields.Str(required=False)
    
    template = fields.Str(required=False)
    

