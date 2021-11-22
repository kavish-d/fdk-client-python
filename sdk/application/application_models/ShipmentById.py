"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .Shipments import Shipments


class ShipmentById(Schema):

    
    shipment = fields.Nested(Shipments, required=False)
    

