"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema




class EmailOtpSuccess(BaseSchema):
    # User swagger.json

    
    success = fields.Boolean(required=False)
    

