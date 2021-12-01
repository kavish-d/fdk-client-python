"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema










class AutocompletePageAction(BaseSchema):

    
    url = fields.Str(required=False)
    
    query = fields.Dict(required=False)
    
    type = fields.Str(required=False)
    
    params = fields.Dict(required=False)
    

