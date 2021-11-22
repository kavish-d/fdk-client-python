"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




















class PlatformShipmentDetailsStatus(Schema):

    
    id = fields.Int(required=False)
    
    bag_list = fields.List(fields.Int(required=False), required=False)
    
    created_at = fields.Str(required=False)
    
    status = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    progress = fields.Int(required=False)
    
    shipment_id = fields.Str(required=False)
    
    current_shipment_status = fields.Str(required=False)
    
    color_code = fields.Str(required=False)
    

