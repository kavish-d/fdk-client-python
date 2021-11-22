"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






















class AddProductCart(Schema):

    
    pos = fields.Boolean(required=False)
    
    item_size = fields.Str(required=False)
    
    article_assignment = fields.Dict(required=False)
    
    article_id = fields.Str(required=False)
    
    seller_id = fields.Int(required=False)
    
    store_id = fields.Int(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    display = fields.Str(required=False)
    
    quantity = fields.Int(required=False)
    
    item_id = fields.Int(required=False)
    

