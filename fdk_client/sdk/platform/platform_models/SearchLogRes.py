"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .LogInfo import LogInfo

from .Page import Page


class SearchLogRes(BaseSchema):
    # Analytics swagger.json

    
    items = fields.List(fields.Nested(LogInfo, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

