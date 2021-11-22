"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class ShipmentTrackResponseBagListItemDpDetails(Schema):

    
    tracking_no = fields.Str(required=False)
    
    courier = fields.Str(required=False)
    

