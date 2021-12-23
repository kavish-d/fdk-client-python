"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema





from .Media import Media

from .ActionPage import ActionPage


class AutocompleteItem(BaseSchema):
    # Catalog swagger.json

    
    display = fields.Str(required=False)
    
    type = fields.Str(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    action = fields.Nested(ActionPage, required=False)
    

