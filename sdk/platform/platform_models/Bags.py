"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .BagItem import BagItem




class Bags(BaseSchema):

    
    item = fields.Nested(BagItem, required=False)
    
    id = fields.Int(required=False)
    

