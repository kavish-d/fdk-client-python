"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .Page import Page

from .ProductTemplate import ProductTemplate


class TemplatesResponse(Schema):

    
    page = fields.Nested(Page, required=False)
    
    items = fields.Nested(ProductTemplate, required=False)
    

