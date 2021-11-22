"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .OrderSchema import OrderSchema


class OrderById(Schema):

    
    order = fields.Nested(OrderSchema, required=False)
    

