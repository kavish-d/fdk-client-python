"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .NavigationSchema import NavigationSchema

from .PageSchema import PageSchema




class PageMetaSchema(BaseSchema):

    
    system_pages = fields.List(fields.Nested(NavigationSchema, required=False), required=False)
    
    custom_pages = fields.List(fields.Nested(PageSchema, required=False), required=False)
    
    application_id = fields.Str(required=False)
    

