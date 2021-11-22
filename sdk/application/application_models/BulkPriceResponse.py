"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .BulkPriceOffer import BulkPriceOffer


class BulkPriceResponse(Schema):

    
    data = fields.List(fields.Nested(BulkPriceOffer, required=False), required=False)
    

