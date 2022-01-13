"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema










class CreateAutocompleteWordsResponse(BaseSchema):
    # Catalog swagger.json

    
    words = fields.List(fields.Str(required=False), required=False)
    
    _custom_json = fields.Dict(required=False)
    
    app_id = fields.Str(required=False)
    
    results = fields.List(fields.Dict(required=False), required=False)
    

