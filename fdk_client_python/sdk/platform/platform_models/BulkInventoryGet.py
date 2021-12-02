"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .BulkInventoryGetItems import BulkInventoryGetItems

from .Page import Page


class BulkInventoryGet(BaseSchema):

    
    items = fields.List(fields.Nested(BulkInventoryGetItems, required=False), required=False)
    
    page = fields.Nested(Page, required=False)
    

