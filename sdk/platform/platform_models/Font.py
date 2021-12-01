"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema



from .Variants import Variants


class Font(BaseSchema):

    
    family = fields.Str(required=False)
    
    variants = fields.Nested(Variants, required=False)
    

