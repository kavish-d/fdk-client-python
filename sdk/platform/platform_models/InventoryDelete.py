"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .InventoryDeleteData import InventoryDeleteData




class InventoryDelete(Schema):

    
    data = fields.Nested(InventoryDeleteData, required=False)
    
    success = fields.Boolean(required=False)
    

