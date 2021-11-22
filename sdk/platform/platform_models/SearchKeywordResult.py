"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class SearchKeywordResult(Schema):

    
    sort_on = fields.Str(required=False)
    
    query = fields.Dict(required=False)
    

