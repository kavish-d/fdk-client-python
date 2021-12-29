"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class UpdatePayoutRequest(BaseSchema):
    # Payment swagger.json

    
    is_default = fields.Boolean(required=False)
    
    is_active = fields.Boolean(required=False)
    
    unique_external_id = fields.Str(required=False)
    

