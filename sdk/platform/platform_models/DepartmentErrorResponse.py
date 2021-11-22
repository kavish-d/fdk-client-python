"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *












class DepartmentErrorResponse(Schema):

    
    meta = fields.Dict(required=False)
    
    message = fields.Str(required=False)
    
    errors = fields.Dict(required=False)
    
    status = fields.Int(required=False)
    
    code = fields.Str(required=False)
    

