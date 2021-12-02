"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema



from .SetSizeDistribution import SetSizeDistribution


class Set(BaseSchema):

    
    quantity = fields.Int(required=False)
    
    size_distribution = fields.Nested(SetSizeDistribution, required=False)
    

