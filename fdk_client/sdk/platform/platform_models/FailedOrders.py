"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .FailOrder import FailOrder


class FailedOrders(BaseSchema):
    # Order swagger.json

    
    orders = fields.Nested(FailOrder, required=False)
    

