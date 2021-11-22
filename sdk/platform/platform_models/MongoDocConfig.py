"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *







from .PropBeanConfig import PropBeanConfig






class MongoDocConfig(Schema):

    
    collection_name = fields.Str(required=False)
    
    find_query = fields.Dict(required=False)
    
    projection_query = fields.Dict(required=False)
    
    prop_bean_configs = fields.List(fields.Nested(PropBeanConfig, required=False), required=False)
    
    aggregate_pipeline = fields.List(fields.Dict(required=False), required=False)
    
    skip_save = fields.Boolean(required=False)
    

