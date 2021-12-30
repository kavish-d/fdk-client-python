"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema









from .ShipmentPromise import ShipmentPromise







from .PaymentSelectionLock import PaymentSelectionLock





from .CartCurrency import CartCurrency



from .ShipmentResponse import ShipmentResponse







from .CartBreakup import CartBreakup


class CartShipmentsResponse(BaseSchema):
    # Cart swagger.json

    
    comment = fields.Str(required=False)
    
    uid = fields.Str(required=False)
    
    message = fields.Str(required=False)
    
    gstin = fields.Str(required=False)
    
    delivery_promise = fields.Nested(ShipmentPromise, required=False)
    
    cart_id = fields.Int(required=False)
    
    checkout_mode = fields.Str(required=False)
    
    error = fields.Boolean(required=False)
    
    payment_selection_lock = fields.Nested(PaymentSelectionLock, required=False)
    
    coupon_text = fields.Str(required=False)
    
    last_modified = fields.Str(required=False)
    
    currency = fields.Nested(CartCurrency, required=False)
    
    delivery_charge_info = fields.Str(required=False)
    
    shipments = fields.List(fields.Nested(ShipmentResponse, required=False), required=False)
    
    id = fields.Str(required=False)
    
    restrict_checkout = fields.Boolean(required=False)
    
    is_valid = fields.Boolean(required=False)
    
    breakup_values = fields.Nested(CartBreakup, required=False)
    
