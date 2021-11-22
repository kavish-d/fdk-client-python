"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .ShortLinkRes import ShortLinkRes

from .Page import Page


class ShortLinkList(Schema):

    
    items = fields.List(fields.Nested(ShortLinkRes, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

