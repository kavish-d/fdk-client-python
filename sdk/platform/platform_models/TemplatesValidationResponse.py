"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .TemplateDetails import TemplateDetails

from .TemplateValidationData import TemplateValidationData


class TemplatesValidationResponse(BaseSchema):

    
    template_details = fields.Nested(TemplateDetails, required=False)
    
    data = fields.Nested(TemplateValidationData, required=False)
    

