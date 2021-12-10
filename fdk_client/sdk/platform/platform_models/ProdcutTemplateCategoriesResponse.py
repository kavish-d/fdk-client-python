"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .Page import Page




class ProdcutTemplateCategoriesResponse(BaseSchema):

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Dict(required=False), required=False)
    

