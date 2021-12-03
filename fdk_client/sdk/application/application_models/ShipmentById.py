"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .Shipments import Shipments


class ShipmentById(BaseSchema):

    
    shipment = fields.Nested(Shipments, required=False)
    

