"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class ShipmentTrackResponseBagListItemsProductImage(Schema):

    
    aspect_ratio = fields.Str(required=False)
    
    url = fields.Str(required=False)
    

