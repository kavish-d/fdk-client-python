"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .Points import Points

from .RewardUser import RewardUser


class UserRes(BaseSchema):

    
    points = fields.Nested(Points, required=False)
    
    user = fields.Nested(RewardUser, required=False)
    
