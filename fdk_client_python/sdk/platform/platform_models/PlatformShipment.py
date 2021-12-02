"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .PlatformShipmentStatus import PlatformShipmentStatus

from .Bags import Bags

from .ShipmentPrices import ShipmentPrices



from .ShipmentGst import ShipmentGst

from .ShipmentBreakupValues import ShipmentBreakupValues










class PlatformShipment(BaseSchema):

    
    status = fields.Nested(PlatformShipmentStatus, required=False)
    
    bags = fields.Nested(Bags, required=False)
    
    prices = fields.Nested(ShipmentPrices, required=False)
    
    id = fields.Str(required=False)
    
    gst = fields.Nested(ShipmentGst, required=False)
    
    breakup_values = fields.Nested(ShipmentBreakupValues, required=False)
    
    priority = fields.Float(required=False)
    
    priority_text = fields.Str(required=False)
    
    lock_status = fields.Boolean(required=False)
    
    total_shipment_bags = fields.Int(required=False)
    

