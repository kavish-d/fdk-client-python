"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .ShipmentTrackResponseBagListItem import ShipmentTrackResponseBagListItem






class ShipmentTrackResponse(Schema):

    
    bag_list = fields.List(fields.Nested(ShipmentTrackResponseBagListItem, required=False), required=False)
    
    message = fields.Str(required=False)
    
    order_value = fields.Int(required=False)
    

