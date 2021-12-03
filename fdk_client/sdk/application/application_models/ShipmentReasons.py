"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .Reasons import Reasons


class ShipmentReasons(BaseSchema):

    
    reasons = fields.List(fields.Nested(Reasons, required=False), required=False)
    

