"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema
















class PayoutsResponse(BaseSchema):
    # Payment swagger.json

    
    is_active = fields.Boolean(required=False)
    
    transfer_type = fields.Str(required=False)
    
    is_default = fields.Boolean(required=False)
    
    more_attributes = fields.Dict(required=False)
    
    payouts_aggregators = fields.List(fields.Dict(required=False), required=False)
    
    unique_transfer_no = fields.Dict(required=False)
    
    customers = fields.Dict(required=False)
    

