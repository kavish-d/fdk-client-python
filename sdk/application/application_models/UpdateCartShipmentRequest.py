"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .UpdateCartShipmentItem import UpdateCartShipmentItem


class UpdateCartShipmentRequest(Schema):

    
    shipments = fields.List(fields.Nested(UpdateCartShipmentItem, required=False), required=False)
    

