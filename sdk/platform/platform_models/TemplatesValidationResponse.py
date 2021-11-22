"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .TemplateValidationData import TemplateValidationData

from .TemplateDetails import TemplateDetails


class TemplatesValidationResponse(Schema):

    
    data = fields.Nested(TemplateValidationData, required=False)
    
    template_details = fields.Nested(TemplateDetails, required=False)
    

