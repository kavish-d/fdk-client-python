"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .FollowIdsData import FollowIdsData


class FollowIdsResponse(Schema):

    
    data = fields.Nested(FollowIdsData, required=False)
    

