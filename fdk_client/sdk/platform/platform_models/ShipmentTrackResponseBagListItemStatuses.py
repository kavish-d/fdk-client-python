"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema





from .ShipmentTrackResponseBagListItemStatusesProgress import ShipmentTrackResponseBagListItemStatusesProgress











from .ShipmentTrackResponseBagListItemStatusesTrack import ShipmentTrackResponseBagListItemStatusesTrack


class ShipmentTrackResponseBagListItemStatuses(BaseSchema):

    
    nps_rating = fields.Int(required=False)
    
    nps_string = fields.Str(required=False)
    
    progress_status = fields.List(fields.Nested(ShipmentTrackResponseBagListItemStatusesProgress, required=False), required=False)
    
    flow_type = fields.Str(required=False)
    
    status_progress = fields.Int(required=False)
    
    is_nps_done = fields.Boolean(required=False)
    
    header_message = fields.Str(required=False)
    
    is_delayed = fields.Str(required=False)
    
    tracking_list = fields.List(fields.Nested(ShipmentTrackResponseBagListItemStatusesTrack, required=False), required=False)
    
