"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .OptType import OptType




class OptedInventory(Schema):

    
    opt_type = fields.Nested(OptType, required=False)
    
    items = fields.Raw(required=False)
    

