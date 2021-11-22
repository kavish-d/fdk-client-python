"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .Timestamp import Timestamp


class Promise(Schema):

    
    timestamp = fields.Nested(Timestamp, required=False)
    

