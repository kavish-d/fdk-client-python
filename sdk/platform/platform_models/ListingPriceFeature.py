"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




class ListingPriceFeature(Schema):

    
    value = fields.Str(required=False)
    

