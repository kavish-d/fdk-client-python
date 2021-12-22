"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema












class InternalDiscountQuery(BaseSchema):
    # Discount swagger.json

    
    job_ids = fields.List(fields.Str(required=False), required=False)
    
    item_ids = fields.List(fields.Int(required=False), required=False)
    
    seller_identifiers = fields.List(fields.Str(required=False), required=False)
    
    brand_ids = fields.List(fields.Int(required=False), required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    

