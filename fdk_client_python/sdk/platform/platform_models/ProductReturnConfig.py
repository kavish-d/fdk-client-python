"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema




class ProductReturnConfig(BaseSchema):

    
    on_same_store = fields.Boolean(required=False)
    

