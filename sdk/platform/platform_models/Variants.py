"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .Medium import Medium

from .SemiBold import SemiBold

from .Bold import Bold

from .Light import Light

from .Regular import Regular


class Variants(Schema):

    
    medium = fields.Nested(Medium, required=False)
    
    semi_bold = fields.Nested(SemiBold, required=False)
    
    bold = fields.Nested(Bold, required=False)
    
    light = fields.Nested(Light, required=False)
    
    regular = fields.Nested(Regular, required=False)
    

