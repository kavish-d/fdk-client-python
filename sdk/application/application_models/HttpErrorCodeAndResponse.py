"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *



from .ErrorCodeAndDescription import ErrorCodeAndDescription


class HttpErrorCodeAndResponse(Schema):

    
    success = fields.Boolean(required=False)
    
    error = fields.Nested(ErrorCodeAndDescription, required=False)
    

