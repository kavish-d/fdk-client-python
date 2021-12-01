"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .UpdateCartShipmentItem import UpdateCartShipmentItem


class UpdateCartShipmentRequest(BaseSchema):

    
    shipments = fields.List(fields.Nested(UpdateCartShipmentItem, required=False), required=False)
    

