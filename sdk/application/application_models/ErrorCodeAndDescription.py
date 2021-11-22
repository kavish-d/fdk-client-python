"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *






class ErrorCodeAndDescription(Schema):

    
    code = fields.Str(required=False)
    
    description = fields.Str(required=False)
    

