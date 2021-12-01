"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..application_enums import *
from ..application_models.BaseSchema import BaseSchema






class OS(BaseSchema):

    
    name = fields.Str(required=False)
    
    version = fields.Str(required=False)
    

