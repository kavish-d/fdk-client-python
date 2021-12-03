"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .RupifiBannerData import RupifiBannerData




class RupifiBannerResponse(BaseSchema):

    
    data = fields.Nested(RupifiBannerData, required=False)
    
    success = fields.Boolean(required=False)
    
