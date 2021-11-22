"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *



from .SizeDistribution import SizeDistribution


class InventorySet(Schema):

    
    quantity = fields.Int(required=False)
    
    size_distribution = fields.Nested(SizeDistribution, required=False)
    

