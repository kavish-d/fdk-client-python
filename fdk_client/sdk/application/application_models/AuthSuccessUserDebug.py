"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema




class AuthSuccessUserDebug(BaseSchema):
    # User swagger.json

    
    platform = fields.Str(required=False)
    

