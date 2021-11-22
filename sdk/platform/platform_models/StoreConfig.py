"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *











from .ProcessConfig import ProcessConfig




class StoreConfig(Schema):

    
    job_code = fields.Str(required=False)
    
    storeid = fields.Str(required=False)
    
    store_alias = fields.Str(required=False)
    
    store_file_regex = fields.Str(required=False)
    
    store_file_name = fields.Str(required=False)
    
    process_config = fields.Nested(ProcessConfig, required=False)
    
    properties = fields.Dict(required=False)
    

