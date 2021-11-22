"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .PromiseFormatted import PromiseFormatted

from .PromiseTimestamp import PromiseTimestamp


class ShipmentPromise(Schema):

    
    formatted = fields.Nested(PromiseFormatted, required=False)
    
    timestamp = fields.Nested(PromiseTimestamp, required=False)
    

