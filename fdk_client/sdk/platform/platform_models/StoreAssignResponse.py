"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema































from .ArticleAssignment1 import ArticleAssignment1




class StoreAssignResponse(BaseSchema):

    
    meta = fields.Dict(required=False)
    
    uid = fields.Str(required=False)
    
    store_id = fields.Int(required=False)
    
    _id = fields.Str(required=False)
    
    store_pincode = fields.Int(required=False)
    
    size = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    index = fields.Int(required=False)
    
    strategy_wise_listing = fields.List(fields.Dict(required=False), required=False)
    
    price_effective = fields.Int(required=False)
    
    price_marked = fields.Int(required=False)
    
    quantity = fields.Int(required=False)
    
    group_id = fields.Str(required=False)
    
    status = fields.Boolean(required=False)
    
    item_id = fields.Int(required=False)
    
    article_assignment = fields.Nested(ArticleAssignment1, required=False)
    
    s_city = fields.Str(required=False)
    
