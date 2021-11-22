"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .AppInventoryStores import AppInventoryStores

from .Page import Page


class StoresResponse(Schema):

    
    items = fields.Nested(AppInventoryStores, required=False)
    
    page = fields.Nested(Page, required=False)
    

