"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .SmsTemplate import SmsTemplate

from .Page import Page


class SmsTemplates(BaseSchema):

    
    items = fields.List(fields.Nested(SmsTemplate, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

