"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *






class InternalServerError(Schema):

    
    message = fields.Str(required=False)
    
    code = fields.Str(required=False)
    

