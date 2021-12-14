"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .Attribute import Attribute



from .UI import UI


class Rating(BaseSchema):
    # Feedback swagger.json

    
    attributes = fields.List(fields.Nested(Attribute, required=False), required=False)
    
    attributes_slugs = fields.List(fields.Str(required=False), required=False)
    
    ui = fields.Nested(UI, required=False)
    

