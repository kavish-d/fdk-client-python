"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class CartItemMeta(BaseSchema):

    
    group_id = fields.Str(required=False)
    
    primary_item = fields.Boolean(required=False)
    
