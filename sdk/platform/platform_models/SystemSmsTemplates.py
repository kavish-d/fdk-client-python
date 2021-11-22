"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .SystemSmsTemplate import SystemSmsTemplate

from .Page import Page


class SystemSmsTemplates(Schema):

    
    items = fields.List(fields.Nested(SystemSmsTemplate, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

