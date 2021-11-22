"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *



from .Variants import Variants


class Font(Schema):

    
    family = fields.Str(required=False)
    
    variants = fields.Nested(Variants, required=False)
    

