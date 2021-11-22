"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *





from .ShipmentResponseReasons import ShipmentResponseReasons


class ShipmentReasonsResponse(Schema):

    
    success = fields.Boolean(required=False)
    
    message = fields.Str(required=False)
    
    reasons = fields.List(fields.Nested(ShipmentResponseReasons, required=False), required=False)
    

