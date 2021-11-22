"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *



from .GlobalValidation import GlobalValidation


class TemplateValidationData(Schema):

    
    template_validation = fields.Dict(required=False)
    
    global_validation = fields.Nested(GlobalValidation, required=False)
    

