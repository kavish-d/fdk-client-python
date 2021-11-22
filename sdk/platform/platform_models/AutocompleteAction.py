"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *



from .AutocompletePageAction import AutocompletePageAction


class AutocompleteAction(Schema):

    
    type = fields.Str(required=False)
    
    page = fields.Nested(AutocompletePageAction, required=False)
    

