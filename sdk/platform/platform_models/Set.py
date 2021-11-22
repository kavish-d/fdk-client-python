"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *



from .SetSizeDistribution import SetSizeDistribution


class Set(Schema):

    
    quantity = fields.Int(required=False)
    
    size_distribution = fields.Nested(SetSizeDistribution, required=False)
    

