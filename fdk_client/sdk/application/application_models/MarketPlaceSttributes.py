"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema



from .Details import Details


class MarketPlaceSttributes(BaseSchema):

    
    title = fields.Str(required=False)
    
    details = fields.List(fields.Nested(Details, required=False), required=False)
    

