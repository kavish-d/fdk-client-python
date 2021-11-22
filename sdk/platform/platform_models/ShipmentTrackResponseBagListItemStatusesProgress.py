"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *








class ShipmentTrackResponseBagListItemStatusesProgress(Schema):

    
    title = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    state = fields.Boolean(required=False)
    

