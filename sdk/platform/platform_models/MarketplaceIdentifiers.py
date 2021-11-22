"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *

from .TatacliqLuxury import TatacliqLuxury


class MarketplaceIdentifiers(Schema):

    
    tatacliq_luxury = fields.Nested(TatacliqLuxury, required=False)
    

