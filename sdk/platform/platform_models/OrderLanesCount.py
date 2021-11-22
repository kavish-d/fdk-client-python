"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .StageItem import StageItem


class OrderLanesCount(Schema):

    
    stages = fields.List(fields.Nested(StageItem, required=False), required=False)
    

