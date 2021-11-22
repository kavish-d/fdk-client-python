"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *



from .Media import Media



from .AutocompleteAction import AutocompleteAction


class AutocompleteResult(Schema):

    
    _custom_json = fields.Dict(required=False)
    
    logo = fields.Nested(Media, required=False)
    
    display = fields.Str(required=False)
    
    action = fields.Nested(AutocompleteAction, required=False)
    

