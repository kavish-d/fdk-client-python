"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .FilerList import FilerList




class InventoryConfig(Schema):

    
    data = fields.List(fields.Nested(FilerList, required=False), required=False)
    
    multivalues = fields.Boolean(required=False)
    

