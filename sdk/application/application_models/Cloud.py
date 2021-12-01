"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema








class Cloud(BaseSchema):

    
    id = fields.Str(required=False)
    
    name = fields.Str(required=False)
    
    provider = fields.Str(required=False)
    

