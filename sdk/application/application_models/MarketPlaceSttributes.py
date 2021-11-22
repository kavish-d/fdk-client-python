"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *



from .Details import Details


class MarketPlaceSttributes(Schema):

    
    title = fields.Str(required=False)
    
    details = fields.List(fields.Nested(Details, required=False), required=False)
    

