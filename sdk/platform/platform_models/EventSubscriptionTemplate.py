"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .EventSubscriptionTemplateSms import EventSubscriptionTemplateSms

from .EventSubscriptionTemplateEmail import EventSubscriptionTemplateEmail


class EventSubscriptionTemplate(Schema):

    
    sms = fields.Nested(EventSubscriptionTemplateSms, required=False)
    
    email = fields.Nested(EventSubscriptionTemplateEmail, required=False)
    

