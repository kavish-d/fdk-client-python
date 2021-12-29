"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema











from .DiscountValueObject import DiscountValueObject














class DiscountDetail(BaseSchema):
    # Discount swagger.json

    
    _id = fields.Str(required=False)
    
    job_id = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    app_ids = fields.List(fields.Str(required=False), required=False)
    
    discount_type = fields.Str(required=False)
    
    discount = fields.List(fields.Nested(DiscountValueObject, required=False), required=False)
    
    brand_ids = fields.List(fields.Int(required=False), required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    item_id = fields.Int(required=False)
    
    seller_identifier = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    

