"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .SystemEmailTemplate import SystemEmailTemplate

from .Page import Page


class SystemEmailTemplates(Schema):

    
    items = fields.List(fields.Nested(SystemEmailTemplate, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

