"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class Closing(BaseSchema):
    # Order swagger.json

    
    hour = fields.Int(required=False)
    
    minute = fields.Int(required=False)
    

