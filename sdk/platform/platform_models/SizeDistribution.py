"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .SetSize import SetSize


class SizeDistribution(BaseSchema):

    
    sizes = fields.List(fields.Nested(SetSize, required=False), required=False)
    

