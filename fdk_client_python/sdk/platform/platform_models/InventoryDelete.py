"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .InventoryDeleteData import InventoryDeleteData




class InventoryDelete(BaseSchema):

    
    data = fields.Nested(InventoryDeleteData, required=False)
    
    success = fields.Boolean(required=False)
    

