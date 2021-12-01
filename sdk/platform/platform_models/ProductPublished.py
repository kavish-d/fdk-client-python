"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class ProductPublished(BaseSchema):

    
    is_set = fields.Boolean(required=False)
    
    product_online_date = fields.Int(required=False)
    

