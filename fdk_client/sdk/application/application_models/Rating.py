"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema

from .Attribute import Attribute



from .UI import UI


class Rating(BaseSchema):

    
    attributes = fields.List(fields.Nested(Attribute, required=False), required=False)
    
    attributes_slugs = fields.List(fields.Str(required=False), required=False)
    
    ui = fields.Nested(UI, required=False)
    
