"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .ProductTemplate import ProductTemplate

from .Page import Page


class TemplatesResponse(BaseSchema):
    # Catalog swagger.json

    
    items = fields.Nested(ProductTemplate, required=False)
    
    page = fields.Nested(Page, required=False)
    

