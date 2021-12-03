"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema







from .TaxLinesPriceSet import TaxLinesPriceSet


class TaxLines(BaseSchema):

    
    title = fields.Str(required=False)
    
    price = fields.Str(required=False)
    
    rate = fields.Int(required=False)
    
    price_set = fields.Nested(TaxLinesPriceSet, required=False)
    

