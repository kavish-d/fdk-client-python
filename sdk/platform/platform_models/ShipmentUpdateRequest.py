"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *










class ShipmentUpdateRequest(Schema):

    
    bags = fields.List(fields.Str(required=False), required=False)
    
    reason = fields.Dict(required=False)
    
    comments = fields.Str(required=False)
    
    action = fields.Str(required=False)
    

