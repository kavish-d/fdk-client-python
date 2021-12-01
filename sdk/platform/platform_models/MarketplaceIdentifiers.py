"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .TatacliqLuxury import TatacliqLuxury


class MarketplaceIdentifiers(BaseSchema):

    
    tatacliq_luxury = fields.Nested(TatacliqLuxury, required=False)
    

