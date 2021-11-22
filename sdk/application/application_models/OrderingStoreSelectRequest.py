"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .OrderingStoreSelect import OrderingStoreSelect


class OrderingStoreSelectRequest(Schema):

    
    ordering_store = fields.Nested(OrderingStoreSelect, required=False)
    

