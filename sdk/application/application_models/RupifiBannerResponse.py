"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *



from .RupifiBannerData import RupifiBannerData


class RupifiBannerResponse(Schema):

    
    success = fields.Boolean(required=False)
    
    data = fields.Nested(RupifiBannerData, required=False)
    

