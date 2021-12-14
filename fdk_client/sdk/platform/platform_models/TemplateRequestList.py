"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .TemplateRequest import TemplateRequest


class TemplateRequestList(BaseSchema):
    # Feedback swagger.json

    
    template_list = fields.List(fields.Nested(TemplateRequest, required=False), required=False)
    

