"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class ProductReturnConfig(Schema):

    
    on_same_store = fields.Boolean(required=False)
    

