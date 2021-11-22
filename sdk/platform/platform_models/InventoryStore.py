"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *





from .AppStoreRules import AppStoreRules


class InventoryStore(Schema):

    
    criteria = fields.Str(required=False)
    
    stores = fields.List(fields.Raw(required=False), required=False)
    
    rules = fields.Nested(AppStoreRules, required=False)
    

