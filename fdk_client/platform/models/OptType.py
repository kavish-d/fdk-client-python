"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class OptType(BaseSchema):
    # Configuration swagger.json

    
    key = fields.Str(required=False)
    
    display = fields.Str(required=False)
    

