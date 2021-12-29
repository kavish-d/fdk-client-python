"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .GlobalValidation import GlobalValidation




class TemplateValidationData(BaseSchema):
    # Catalog swagger.json

    
    global_validation = fields.Nested(GlobalValidation, required=False)
    
    template_validation = fields.Dict(required=False)
    

