"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .OrderSchema import OrderSchema


class OrderById(BaseSchema):

    
    order = fields.Nested(OrderSchema, required=False)
    

