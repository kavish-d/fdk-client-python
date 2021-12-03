"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class SearchKeywordResult(BaseSchema):

    
    query = fields.Dict(required=False)
    
    sort_on = fields.Str(required=False)
    
