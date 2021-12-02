"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .ShortLinkRes import ShortLinkRes

from .Page import Page


class ShortLinkList(BaseSchema):

    
    items = fields.List(fields.Nested(ShortLinkRes, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

