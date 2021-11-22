"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *










class AutocompletePageAction(Schema):

    
    type = fields.Str(required=False)
    
    params = fields.Dict(required=False)
    
    url = fields.Str(required=False)
    
    query = fields.Dict(required=False)
    

