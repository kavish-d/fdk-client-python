"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .Items import Items

from .Page import Page


class BulkAssetResponse(BaseSchema):

    
    items = fields.List(fields.Nested(Items, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

