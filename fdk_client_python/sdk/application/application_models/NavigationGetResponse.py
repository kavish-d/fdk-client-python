"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .NavigationSchema import NavigationSchema

from .Page import Page


class NavigationGetResponse(BaseSchema):

    
    items = fields.List(fields.Nested(NavigationSchema, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

