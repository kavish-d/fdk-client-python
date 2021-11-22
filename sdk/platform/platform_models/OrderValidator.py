"""Class Validators."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

class OrderValidator:
    
    class shipmentStatusUpdate(Schema):
        
        company_id = fields.Str(required=False)
         
    
    class activityStatus(Schema):
        
        company_id = fields.Str(required=False)
        
        bag_id = fields.Str(required=False)
         
    
    class storeProcessShipmentUpdate(Schema):
        
        company_id = fields.Str(required=False)
         
    
    class checkRefund(Schema):
        
        company_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
         
    
    class ShipmentBagsCanBreak(Schema):
        
        company_id = fields.Str(required=False)
         
    
    class getOrdersByCompanyId(Schema):
        
        company_id = fields.Str(required=False)
        
        page_no = fields.Str(required=False)
        
        page_size = fields.Str(required=False)
        
        from_date = fields.Str(required=False)
        
        to_date = fields.Str(required=False)
        
        q = fields.Str(required=False)
        
        stage = fields.Str(required=False)
        
        sales_channels = fields.Str(required=False)
        
        order_id = fields.Str(required=False)
        
        stores = fields.Str(required=False)
        
        deployment_stores = fields.Str(required=False)
        
        status = fields.Str(required=False)
        
        dp = fields.Str(required=False)
        
        shorten_urls = fields.Boolean(required=False)
        
        filter_type = fields.Str(required=False)
         
    
    class getOrderLanesCountByCompanyId(Schema):
        
        company_id = fields.Str(required=False)
        
        page_no = fields.Str(required=False)
        
        page_size = fields.Str(required=False)
        
        from_date = fields.Str(required=False)
        
        to_date = fields.Str(required=False)
        
        q = fields.Str(required=False)
        
        stage = fields.Str(required=False)
        
        sales_channels = fields.Str(required=False)
        
        order_id = fields.Str(required=False)
        
        stores = fields.Str(required=False)
        
        status = fields.Str(required=False)
        
        shorten_urls = fields.Boolean(required=False)
        
        filter_type = fields.Str(required=False)
         
    
    class getOrderDetails(Schema):
        
        company_id = fields.Str(required=False)
        
        order_id = fields.Str(required=False)
        
        next = fields.Str(required=False)
        
        previous = fields.Str(required=False)
         
    
    class getPicklistOrdersByCompanyId(Schema):
        
        company_id = fields.Str(required=False)
        
        page_no = fields.Str(required=False)
        
        page_size = fields.Str(required=False)
        
        from_date = fields.Str(required=False)
        
        to_date = fields.Str(required=False)
        
        q = fields.Str(required=False)
        
        stage = fields.Str(required=False)
        
        sales_channels = fields.Str(required=False)
        
        order_id = fields.Str(required=False)
        
        stores = fields.Str(required=False)
        
        status = fields.Str(required=False)
        
        shorten_urls = fields.Boolean(required=False)
        
        filter_type = fields.Str(required=False)
         
    
    class trackShipmentPlatform(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
         
    
    class trackOrder(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        order_id = fields.Str(required=False)
         
    
    class failedOrders(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
         
    
    class reprocessOrder(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        order_id = fields.Str(required=False)
         
    
    class updateShipment(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
         
    
    class getPlatformShipmentReasons(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        action = fields.Str(required=False)
         
    
    class getShipmentTrackDetails(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        order_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
         
    
    class getShipmentAddress(Schema):
        
        company_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
        
        address_category = fields.Str(required=False)
         
    
    class updateShipmentAddress(Schema):
        
        company_id = fields.Str(required=False)
        
        shipment_id = fields.Str(required=False)
        
        address_category = fields.Str(required=False)
         
    
    class getOrdersByApplicationId(Schema):
        
        company_id = fields.Str(required=False)
        
        application_id = fields.Str(required=False)
        
        page_no = fields.Str(required=False)
        
        page_size = fields.Str(required=False)
        
        from_date = fields.Str(required=False)
        
        to_date = fields.Str(required=False)
        
        q = fields.Str(required=False)
        
        stage = fields.Str(required=False)
        
        sales_channels = fields.Str(required=False)
        
        order_id = fields.Str(required=False)
        
        stores = fields.Str(required=False)
        
        status = fields.Str(required=False)
        
        dp = fields.Str(required=False)
        
        shorten_urls = fields.Boolean(required=False)
        
        filter_type = fields.Str(required=False)
         
    
    class getPing(Schema):
        
        company_id = fields.Str(required=False)
         
    
    class voiceCallback(Schema):
        
        company_id = fields.Str(required=False)
         
    
    class voiceClickToCall(Schema):
        
        company_id = fields.Str(required=False)
        
        caller = fields.Str(required=False)
        
        receiver = fields.Str(required=False)
         
    