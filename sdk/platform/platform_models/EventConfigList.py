"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .EventConfig import EventConfig

from .Page import Page


class EventConfigList(BaseSchema):

    
    items = fields.List(fields.Nested(EventConfig, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

