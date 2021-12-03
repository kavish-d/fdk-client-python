"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class Android(BaseSchema):

    
    application_id = fields.Str(required=False)
    
    api_key = fields.Str(required=False)
    
