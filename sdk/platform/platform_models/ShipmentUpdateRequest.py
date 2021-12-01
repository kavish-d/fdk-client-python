"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema










class ShipmentUpdateRequest(BaseSchema):

    
    bags = fields.List(fields.Str(required=False), required=False)
    
    reason = fields.Dict(required=False)
    
    comments = fields.Str(required=False)
    
    action = fields.Str(required=False)
    

