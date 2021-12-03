"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema




class SecureUrl(BaseSchema):

    
    secure_url = fields.Str(required=False)
    
