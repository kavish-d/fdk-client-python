"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class RewardsAudience(BaseSchema):
    # Rewards swagger.json

    
    header_user_id = fields.Str(required=False)
    
    id = fields.Str(required=False)
    

