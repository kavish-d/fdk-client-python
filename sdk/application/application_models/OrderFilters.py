"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .OrderStatuses import OrderStatuses


class OrderFilters(Schema):

    
    statuses = fields.List(fields.Nested(OrderStatuses, required=False), required=False)
    

