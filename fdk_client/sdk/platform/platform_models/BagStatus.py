"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema







from .BagStatusBagStateMapper import BagStatusBagStateMapper


class BagStatus(BaseSchema):
    # Order swagger.json

    
    status = fields.Str(required=False)
    
    state_type = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    bag_state_mapper = fields.Nested(BagStatusBagStateMapper, required=False)
    

