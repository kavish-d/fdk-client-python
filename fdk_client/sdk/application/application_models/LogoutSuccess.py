"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema




class LogoutSuccess(BaseSchema):
    # User swagger.json

    
    logout = fields.Boolean(required=False)
    

