"""Application Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class Debug(BaseSchema):
    # Lead swagger.json

    
    source = fields.Str(required=False)
    
    platform = fields.Str(required=False)
    

