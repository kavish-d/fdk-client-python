"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .BagItem import BagItem




class Bags(Schema):

    
    item = fields.Nested(BagItem, required=False)
    
    id = fields.Int(required=False)
    

