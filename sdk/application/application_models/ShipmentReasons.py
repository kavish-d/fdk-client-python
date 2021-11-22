"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .Reasons import Reasons


class ShipmentReasons(Schema):

    
    reasons = fields.List(fields.Nested(Reasons, required=False), required=False)
    

