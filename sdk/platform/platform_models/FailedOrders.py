"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .FailOrder import FailOrder


class FailedOrders(Schema):

    
    orders = fields.Nested(FailOrder, required=False)
    

