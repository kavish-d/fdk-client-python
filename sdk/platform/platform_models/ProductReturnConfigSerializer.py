"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class ProductReturnConfigSerializer(Schema):

    
    on_same_store = fields.Boolean(required=False)
    
    store_uid = fields.Int(required=False)
    

