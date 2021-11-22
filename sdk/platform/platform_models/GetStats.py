"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .Stats import Stats


class GetStats(Schema):

    
    items = fields.List(fields.Nested(Stats, required=False), required=False)
    

