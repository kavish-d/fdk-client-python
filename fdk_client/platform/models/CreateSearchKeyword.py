"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema



from .SearchKeywordResult import SearchKeywordResult








class CreateSearchKeyword(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    result = fields.Nested(SearchKeywordResult, required=False)
    
    is_active = fields.Boolean(required=False)
    
    words = fields.List(fields.Str(required=False), required=False)
    
    app_id = fields.Str(required=False)
    

