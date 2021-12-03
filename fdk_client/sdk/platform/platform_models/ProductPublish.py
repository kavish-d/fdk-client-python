"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class ProductPublish(BaseSchema):

    
    product_online_date = fields.Str(required=False)
    
    is_set = fields.Boolean(required=False)
    

