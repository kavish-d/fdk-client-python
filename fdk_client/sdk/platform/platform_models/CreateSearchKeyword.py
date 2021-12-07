"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema





from .SearchKeywordResult import SearchKeywordResult






class CreateSearchKeyword(BaseSchema):

    
    _custom_json = fields.Dict(required=False)
    
    is_active = fields.Boolean(required=False)
    
    result = fields.Nested(SearchKeywordResult, required=False)
    
    app_id = fields.Str(required=False)
    
    words = fields.List(fields.Str(required=False), required=False)
    

