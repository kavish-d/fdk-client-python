"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .Page import Page

from .BulkInventoryGetItems import BulkInventoryGetItems


class BulkInventoryGet(Schema):

    
    page = fields.Nested(Page, required=False)
    
    items = fields.List(fields.Nested(BulkInventoryGetItems, required=False), required=False)
    

