"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .Timestamp import Timestamp


class Promise(BaseSchema):

    
    timestamp = fields.Nested(Timestamp, required=False)
    

