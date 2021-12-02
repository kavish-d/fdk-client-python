"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .StatGroup import StatGroup


class StatsGroups(BaseSchema):

    
    groups = fields.List(fields.Nested(StatGroup, required=False), required=False)
    

