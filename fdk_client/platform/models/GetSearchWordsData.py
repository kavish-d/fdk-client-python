"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class GetSearchWordsData(BaseSchema):
    # Catalog swagger.json

    
    _custom_json = fields.Dict(required=False)
    
    uid = fields.Str(required=False)
    
    result = fields.Dict(required=False)
    
    words = fields.List(fields.Str(required=False), required=False)
    
    app_id = fields.Str(required=False)
    

