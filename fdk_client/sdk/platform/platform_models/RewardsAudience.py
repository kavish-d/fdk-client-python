"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class RewardsAudience(BaseSchema):

    
    header_user_id = fields.Str(required=False)
    
    id = fields.Str(required=False)
    
