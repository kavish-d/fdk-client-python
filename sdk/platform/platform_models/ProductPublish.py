"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class ProductPublish(Schema):

    
    is_set = fields.Boolean(required=False)
    
    product_online_date = fields.Str(required=False)
    

