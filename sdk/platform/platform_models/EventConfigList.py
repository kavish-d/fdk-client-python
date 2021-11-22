"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .EventConfig import EventConfig

from .Page import Page


class EventConfigList(Schema):

    
    items = fields.List(fields.Nested(EventConfig, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

