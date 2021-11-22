"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .TemplateRequest import TemplateRequest


class TemplateRequestList(Schema):

    
    template_list = fields.List(fields.Nested(TemplateRequest, required=False), required=False)
    

