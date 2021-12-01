"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .SystemSmsTemplate import SystemSmsTemplate

from .Page import Page


class SystemSmsTemplates(BaseSchema):

    
    items = fields.List(fields.Nested(SystemSmsTemplate, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

