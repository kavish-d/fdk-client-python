"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class EventSubscriptionTemplateEmail(Schema):

    
    subscribed = fields.Boolean(required=False)
    
    template = fields.Str(required=False)
    

