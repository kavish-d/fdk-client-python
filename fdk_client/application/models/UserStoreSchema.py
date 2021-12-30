"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema












class UserStoreSchema(BaseSchema):
    # User swagger.json

    
    user_id = fields.Str(required=False)
    
    data = fields.Dict(required=False)
    
    _id = fields.Str(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    

