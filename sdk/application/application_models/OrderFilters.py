"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .OrderStatuses import OrderStatuses


class OrderFilters(BaseSchema):

    
    statuses = fields.List(fields.Nested(OrderStatuses, required=False), required=False)
    

