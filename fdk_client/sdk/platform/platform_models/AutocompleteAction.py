"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema



from .AutocompletePageAction import AutocompletePageAction


class AutocompleteAction(BaseSchema):

    
    type = fields.Str(required=False)
    
    page = fields.Nested(AutocompletePageAction, required=False)
    

