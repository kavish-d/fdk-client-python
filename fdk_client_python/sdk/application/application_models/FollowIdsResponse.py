"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .FollowIdsData import FollowIdsData


class FollowIdsResponse(BaseSchema):

    
    data = fields.Nested(FollowIdsData, required=False)
    

