"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema



from .SizeDistribution import SizeDistribution


class InventorySet(BaseSchema):

    
    quantity = fields.Int(required=False)
    
    size_distribution = fields.Nested(SizeDistribution, required=False)
    

