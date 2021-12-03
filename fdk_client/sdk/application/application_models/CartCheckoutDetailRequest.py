"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema



from .StaffCheckout import StaffCheckout






























class CartCheckoutDetailRequest(BaseSchema):

    
    billing_address_id = fields.Str(required=False)
    
    staff = fields.Nested(StaffCheckout, required=False)
    
    payment_auto_confirm = fields.Boolean(required=False)
    
    fyndstore_emp_id = fields.Str(required=False)
    
    extra_meta = fields.Dict(required=False)
    
    aggregator = fields.Str(required=False)
    
    payment_mode = fields.Str(required=False)
    
    address_id = fields.Str(required=False)
    
    payment_identifier = fields.Str(required=False)
    
    payment_params = fields.Dict(required=False)
    
    merchant_code = fields.Str(required=False)
    
    ordering_store = fields.Int(required=False)
    
    callback_url = fields.Str(required=False)
    
    meta = fields.Dict(required=False)
    
    delivery_address = fields.Dict(required=False)
    
    billing_address = fields.Dict(required=False)
    
