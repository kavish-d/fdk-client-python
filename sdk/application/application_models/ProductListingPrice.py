"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *

from .Price import Price

from .Price import Price


class ProductListingPrice(Schema):

    
    effective = fields.Nested(Price, required=False)
    
    marked = fields.Nested(Price, required=False)
    

