"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *





from .SearchKeywordResult import SearchKeywordResult






class CreateSearchKeyword(Schema):

    
    _custom_json = fields.Dict(required=False)
    
    app_id = fields.Str(required=False)
    
    result = fields.Nested(SearchKeywordResult, required=False)
    
    is_active = fields.Boolean(required=False)
    
    words = fields.List(fields.Str(required=False), required=False)
    

