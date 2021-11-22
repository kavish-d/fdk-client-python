"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *



from .StatsGroupComponent import StatsGroupComponent


class StatsGroupComponents(Schema):

    
    title = fields.Str(required=False)
    
    components = fields.List(fields.Nested(StatsGroupComponent, required=False), required=False)
    

