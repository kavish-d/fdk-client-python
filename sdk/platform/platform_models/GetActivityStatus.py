"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .ActivityHistory import ActivityHistory


class GetActivityStatus(Schema):

    
    activity_history = fields.Nested(ActivityHistory, required=False)
    

