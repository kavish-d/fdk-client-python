"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



























from .Files import Files







from .StaffCheckout import StaffCheckout






class CartPosCheckoutDetailRequest(BaseSchema):
    # PosCart swagger.json

    
    order_type = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    merchant_code = fields.Str(required=False)
    
    billing_address_id = fields.Str(required=False)
    
    pos = fields.Boolean(required=False)
    
    payment_params = fields.Dict(required=False)
    
    payment_mode = fields.Str(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    payment_auto_confirm = fields.Boolean(required=False)
    
    ordering_store = fields.Int(required=False)
    
    fyndstore_emp_id = fields.Str(required=False)
    
    delivery_address = fields.Dict(required=False)
    
    billing_address = fields.Dict(required=False)
    
    files = fields.List(fields.Nested(Files, required=False), required=False)
    
    meta = fields.Dict(required=False)
    
    pick_at_store_uid = fields.Int(required=False)
    
    address_id = fields.Str(required=False)
    
    staff = fields.Nested(StaffCheckout, required=False)
    
    callback_url = fields.Str(required=False)
    
    aggregator = fields.Str(required=False)
    

