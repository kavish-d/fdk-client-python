"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .AutocompleteAction import AutocompleteAction



from .Media import Media




class AutocompleteResult(BaseSchema):

    
    action = fields.Nested(AutocompleteAction, required=False)
    
    _custom_json = fields.Dict(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    display = fields.Str(required=False)
    
