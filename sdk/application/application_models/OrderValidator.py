"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

class OrderValidator:
    
    class getOrders(Schema):
        
        page_no = fields.Int(required=False)
        
        page_size = fields.Int(required=False)
        
        from_date = fields.Str(required=False)
        
        to_date = fields.Str(required=False)
        
        status = fields.Int(required=False)
         
    
    class getOrderById(Schema):
        
        order_id = fields.Str(required=False)
         
    
    class getShipmentById(Schema):
        
        shipment_id = fields.Str(required=False)
         
    
    class getShipmentReasons(Schema):
        
        shipment_id = fields.Str(required=False)
         
    
    class updateShipmentStatus(Schema):
        
        shipment_id = fields.Str(required=False)
         
    
    class trackShipment(Schema):
        
        shipment_id = fields.Str(required=False)
         
    
    class getPosOrderById(Schema):
        
        order_id = fields.Str(required=False)
         
    
    class getCustomerDetailsByShipmentId(Schema):
        
        order_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
         
    
    class sendOtpToShipmentCustomer(Schema):
        
        order_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
         
    
    class verifyOtpShipmentCustomer(Schema):
        
        order_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
         
    