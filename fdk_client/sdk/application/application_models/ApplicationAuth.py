"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema




class ApplicationAuth(BaseSchema):
    # Configuration swagger.json

    
    enabled = fields.Boolean(required=False)
    

