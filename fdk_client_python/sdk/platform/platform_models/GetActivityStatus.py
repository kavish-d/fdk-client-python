"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .ActivityHistory import ActivityHistory


class GetActivityStatus(BaseSchema):

    
    activity_history = fields.Nested(ActivityHistory, required=False)
    

