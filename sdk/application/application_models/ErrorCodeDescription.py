"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *








class ErrorCodeDescription(Schema):

    
    success = fields.Boolean(required=False)
    
    code = fields.Str(required=False)
    
    description = fields.Str(required=False)
    

