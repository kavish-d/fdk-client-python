"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema












class GetSearchWordsData(BaseSchema):

    
    _custom_json = fields.Dict(required=False)
    
    result = fields.Dict(required=False)
    
    words = fields.List(fields.Str(required=False), required=False)
    
    uid = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    

