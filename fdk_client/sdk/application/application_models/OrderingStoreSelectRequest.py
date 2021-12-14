"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .OrderingStoreSelect import OrderingStoreSelect


class OrderingStoreSelectRequest(BaseSchema):
    # Configuration swagger.json

    
    ordering_store = fields.Nested(OrderingStoreSelect, required=False)
    

