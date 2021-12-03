"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema



from .BreakupValues import BreakupValues



from .Shipments import Shipments



from .UserInfo import UserInfo

from .BagsForReorder import BagsForReorder


class OrderSchema(BaseSchema):

    
    order_id = fields.Str(required=False)
    
    breakup_values = fields.List(fields.Nested(BreakupValues, required=False), required=False)
    
    order_created_time = fields.Str(required=False)
    
    shipments = fields.List(fields.Nested(Shipments, required=False), required=False)
    
    total_shipments_in_order = fields.Int(required=False)
    
    user_info = fields.Nested(UserInfo, required=False)
    
    bags_for_reorder = fields.List(fields.Nested(BagsForReorder, required=False), required=False)
    
