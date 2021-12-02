"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema

from .AssignStoreArticle import AssignStoreArticle














class AssignStore(BaseSchema):

    
    articles = fields.List(fields.Nested(AssignStoreArticle, required=False), required=False)
    
    channel_type = fields.Str(required=False)
    
    company_id = fields.Int(required=False)
    
    store_ids = fields.List(fields.Int(required=False), required=False)
    
    pincode = fields.Str(required=False)
    
    app_id = fields.Str(required=False)
    
    channel_identifier = fields.Str(required=False)
    

