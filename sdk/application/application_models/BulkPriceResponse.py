"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .BulkPriceOffer import BulkPriceOffer


class BulkPriceResponse(BaseSchema):

    
    data = fields.List(fields.Nested(BulkPriceOffer, required=False), required=False)
    

