"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..enums import *
from ..models.BaseSchema import BaseSchema






class PromiseTimestamp(BaseSchema):
    # Cart swagger.json

    
    max = fields.Float(required=False)
    
    min = fields.Float(required=False)
    

