"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .StoreDetail import StoreDetail

from .Page import Page


class OptinStoreDetails(BaseSchema):

    
    items = fields.List(fields.Nested(StoreDetail, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

