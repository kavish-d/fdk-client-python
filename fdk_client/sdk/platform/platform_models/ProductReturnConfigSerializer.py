"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class ProductReturnConfigSerializer(BaseSchema):

    
    store_uid = fields.Int(required=False)
    
    on_same_store = fields.Boolean(required=False)
    

