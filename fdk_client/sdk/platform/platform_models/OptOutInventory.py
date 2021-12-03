"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema






class OptOutInventory(BaseSchema):

    
    store = fields.List(fields.Int(required=False), required=False)
    
    company = fields.List(fields.Int(required=False), required=False)
    
