"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .SetSize import SetSize


class SizeDistribution(Schema):

    
    sizes = fields.List(fields.Nested(SetSize, required=False), required=False)
    

