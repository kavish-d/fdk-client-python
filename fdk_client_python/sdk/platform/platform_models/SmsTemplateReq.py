"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema





from .SmsTemplateMessage import SmsTemplateMessage








class SmsTemplateReq(BaseSchema):

    
    name = fields.Str(required=False)
    
    description = fields.Str(required=False)
    
    message = fields.Nested(SmsTemplateMessage, required=False)
    
    template_variables = fields.Raw(required=False)
    
    attachments = fields.List(fields.Raw(required=False), required=False)
    
    priority = fields.Str(required=False)
    

