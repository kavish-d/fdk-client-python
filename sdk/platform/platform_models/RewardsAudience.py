"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class RewardsAudience(Schema):

    
    header_user_id = fields.Str(required=False)
    
    id = fields.Str(required=False)
    

