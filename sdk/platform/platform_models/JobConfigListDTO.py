"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *


















class JobConfigListDTO(Schema):

    
    code = fields.Str(required=False)
    
    alias = fields.Str(required=False)
    
    modified_by = fields.Str(required=False)
    
    created_by = fields.Str(required=False)
    
    modified_on = fields.Str(required=False)
    
    created_on = fields.Str(required=False)
    
    active = fields.Boolean(required=False)
    
    type = fields.Str(required=False)
    

