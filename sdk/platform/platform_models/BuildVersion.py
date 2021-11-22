"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *




















class BuildVersion(Schema):

    
    _id = fields.Str(required=False)
    
    application = fields.Str(required=False)
    
    platform_type = fields.Str(required=False)
    
    build_status = fields.Str(required=False)
    
    version_name = fields.Str(required=False)
    
    version_code = fields.Int(required=False)
    
    created_at = fields.Str(required=False)
    
    updated_at = fields.Str(required=False)
    
    __v = fields.Int(required=False)
    

