"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema












class DepartmentErrorResponse(BaseSchema):

    
    status = fields.Int(required=False)
    
    code = fields.Str(required=False)
    
    errors = fields.Dict(required=False)
    
    meta = fields.Dict(required=False)
    
    message = fields.Str(required=False)
    

