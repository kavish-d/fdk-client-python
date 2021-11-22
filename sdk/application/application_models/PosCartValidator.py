"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

class PosCartValidator:
    
    class getCart(Schema):
        
        id = fields.Str(required=False)
        
        i = fields.Boolean(required=False)
        
        b = fields.Boolean(required=False)
        
        assign_card_id = fields.Int(required=False)
         
    
    class getCartLastModified(Schema):
        
        id = fields.Str(required=False)
         
    
    class addItems(Schema):
        
        i = fields.Boolean(required=False)
        
        b = fields.Boolean(required=False)
         
    
    class updateCart(Schema):
        
        id = fields.Str(required=False)
        
        i = fields.Boolean(required=False)
        
        b = fields.Boolean(required=False)
         
    
    class getItemCount(Schema):
        
        id = fields.Str(required=False)
         
    
    class getCoupons(Schema):
        
        id = fields.Str(required=False)
         
    
    class applyCoupon(Schema):
        
        i = fields.Boolean(required=False)
        
        b = fields.Boolean(required=False)
        
        p = fields.Boolean(required=False)
        
        id = fields.Str(required=False)
         
    
    class removeCoupon(Schema):
        
        id = fields.Str(required=False)
         
    
    class getBulkDiscountOffers(Schema):
        
        item_id = fields.Int(required=False)
        
        article_id = fields.Str(required=False)
        
        uid = fields.Int(required=False)
        
        slug = fields.Str(required=False)
         
    
    class applyRewardPoints(Schema):
        
        id = fields.Str(required=False)
        
        i = fields.Boolean(required=False)
        
        b = fields.Boolean(required=False)
         
    
    class getAddresses(Schema):
        
        cart_id = fields.Str(required=False)
        
        mobile_no = fields.Str(required=False)
        
        checkout_mode = fields.Str(required=False)
        
        tags = fields.Str(required=False)
        
        is_default = fields.Boolean(required=False)
         
    
    class addAddress(Schema):
        
        pass 
    
    class getAddressById(Schema):
        
        id = fields.Str(required=False)
        
        cart_id = fields.Str(required=False)
        
        mobile_no = fields.Str(required=False)
        
        checkout_mode = fields.Str(required=False)
        
        tags = fields.Str(required=False)
        
        is_default = fields.Boolean(required=False)
         
    
    class updateAddress(Schema):
        
        id = fields.Str(required=False)
         
    
    class removeAddress(Schema):
        
        id = fields.Str(required=False)
         
    
    class selectAddress(Schema):
        
        cart_id = fields.Str(required=False)
        
        i = fields.Boolean(required=False)
        
        b = fields.Boolean(required=False)
         
    
    class selectPaymentMode(Schema):
        
        id = fields.Str(required=False)
         
    
    class validateCouponForPayment(Schema):
        
        id = fields.Str(required=False)
        
        address_id = fields.Str(required=False)
        
        payment_mode = fields.Str(required=False)
        
        payment_identifier = fields.Str(required=False)
        
        aggregator_name = fields.Str(required=False)
        
        merchant_code = fields.Str(required=False)
         
    
    class getShipments(Schema):
        
        pick_at_store_uid = fields.Int(required=False)
        
        ordering_store_id = fields.Int(required=False)
        
        p = fields.Boolean(required=False)
        
        id = fields.Str(required=False)
        
        address_id = fields.Str(required=False)
        
        area_code = fields.Str(required=False)
        
        order_type = fields.Str(required=False)
         
    
    class updateShipments(Schema):
        
        i = fields.Boolean(required=False)
        
        p = fields.Boolean(required=False)
        
        id = fields.Str(required=False)
        
        address_id = fields.Str(required=False)
        
        order_type = fields.Str(required=False)
         
    
    class checkoutCart(Schema):
        
        id = fields.Str(required=False)
         
    
    class updateCartMeta(Schema):
        
        id = fields.Str(required=False)
         
    
    class getAvailableDeliveryModes(Schema):
        
        area_code = fields.Str(required=False)
        
        id = fields.Str(required=False)
         
    
    class getStoreAddressByUid(Schema):
        
        store_uid = fields.Int(required=False)
         
    
    class getCartShareLink(Schema):
        
        pass 
    
    class getCartSharedItems(Schema):
        
        token = fields.Str(required=False)
         
    
    class updateCartWithSharedItems(Schema):
        
        token = fields.Str(required=False)
        
        action = fields.Str(required=False)
         
    