"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema




class ResetPasswordSuccess(BaseSchema):
    # User swagger.json

    
    status = fields.Str(required=False)
    

