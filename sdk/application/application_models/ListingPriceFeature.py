"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *




class ListingPriceFeature(Schema):

    
    value = fields.Str(required=False)
    

