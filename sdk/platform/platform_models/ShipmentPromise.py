"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .PromiseTimestamp import PromiseTimestamp

from .PromiseFormatted import PromiseFormatted


class ShipmentPromise(Schema):

    
    timestamp = fields.Nested(PromiseTimestamp, required=False)
    
    formatted = fields.Nested(PromiseFormatted, required=False)
    

