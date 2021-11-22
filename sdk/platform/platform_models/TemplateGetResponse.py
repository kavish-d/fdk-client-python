"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .Template import Template

from .Page import Page


class TemplateGetResponse(Schema):

    
    items = fields.List(fields.Nested(Template, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

