"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .Timestamp import Timestamp


class Promise(BaseSchema):
    # Order swagger.json

    
    timestamp = fields.Nested(Timestamp, required=False)
    

