"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class ShipmentResponseReasons(Schema):

    
    reason_id = fields.Float(required=False)
    
    reason = fields.Str(required=False)
    

