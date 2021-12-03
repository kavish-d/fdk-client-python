"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class ShipmentTrackResponseBagListItemDpDetails(BaseSchema):

    
    tracking_no = fields.Str(required=False)
    
    courier = fields.Str(required=False)
    

