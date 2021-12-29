"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .FilerList import FilerList




class InventoryConfig(BaseSchema):
    # Catalog swagger.json

    
    data = fields.List(fields.Nested(FilerList, required=False), required=False)
    
    multivalues = fields.Boolean(required=False)
    

