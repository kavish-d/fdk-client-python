"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .ShippingAddress import ShippingAddress

from .OpenApiOrderItem import OpenApiOrderItem





from .ShippingAddress import ShippingAddress





from .OpenApiFiles import OpenApiFiles





from .MultiTenderPaymentMethod import MultiTenderPaymentMethod








class OpenApiPlatformCheckoutReq(BaseSchema):
    # Cart swagger.json

    
    currency_code = fields.Str(required=False)
    
    cod_charges = fields.Float(required=False)
    
    coupon = fields.Str(required=False)
    
    employee_discount = fields.Dict(required=False)
    
    billing_address = fields.Nested(ShippingAddress, required=False)
    
    cart_items = fields.List(fields.Nested(OpenApiOrderItem, required=False), required=False)
    
    coupon_value = fields.Float(required=False)
    
    delivery_charges = fields.Float(required=False)
    
    shipping_address = fields.Nested(ShippingAddress, required=False)
    
    order_id = fields.Str(required=False)
    
    cart_value = fields.Float(required=False)
    
    files = fields.List(fields.Nested(OpenApiFiles, required=False), required=False)
    
    coupon_code = fields.Str(required=False)
    
    loyalty_discount = fields.Float(required=False)
    
    payment_methods = fields.List(fields.Nested(MultiTenderPaymentMethod, required=False), required=False)
    
    payment_mode = fields.Str(required=False)
    
    cashback_applied = fields.Float(required=False)
    
    affiliate_order_id = fields.Str(required=False)
    

