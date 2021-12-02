"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .EventSubscription import EventSubscription

from .Page import Page


class EventSubscriptions(BaseSchema):

    
    items = fields.List(fields.Nested(EventSubscription, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

