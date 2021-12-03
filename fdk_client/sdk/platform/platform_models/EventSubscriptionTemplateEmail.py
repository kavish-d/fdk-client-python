"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class EventSubscriptionTemplateEmail(BaseSchema):

    
    subscribed = fields.Boolean(required=False)
    
    template = fields.Str(required=False)
    
