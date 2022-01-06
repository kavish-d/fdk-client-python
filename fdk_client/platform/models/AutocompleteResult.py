"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .AutocompleteAction import AutocompleteAction

from .Media import Media




class AutocompleteResult(BaseSchema):
    # Catalog swagger.json

    
    display = fields.Str(required=False)
    
    action = fields.Nested(AutocompleteAction, required=False)
    
    logo = fields.Nested(Media, required=False)
    
    _custom_json = fields.Dict(required=False)
    

