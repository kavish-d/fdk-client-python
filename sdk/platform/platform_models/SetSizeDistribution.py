"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .Sizes import Sizes


class SetSizeDistribution(Schema):

    
    sizes = fields.Nested(Sizes, required=False)
    

