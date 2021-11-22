"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .StatGroup import StatGroup


class StatsGroups(Schema):

    
    groups = fields.List(fields.Nested(StatGroup, required=False), required=False)
    

