"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .Track import Track


class ShipmentTrack(Schema):

    
    results = fields.List(fields.Nested(Track, required=False), required=False)
    

