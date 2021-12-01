"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .Details import Details




class MarketPlaceSttributes(BaseSchema):

    
    details = fields.List(fields.Nested(Details, required=False), required=False)
    
    title = fields.Str(required=False)
    

