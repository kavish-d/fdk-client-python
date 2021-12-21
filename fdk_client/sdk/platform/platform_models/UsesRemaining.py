"""Platform Models."""

from marshmallow import fields, Schema
from marshmallow.validate import OneOf
from ..platform_enums import *
from ..platform_models.BaseSchema import BaseSchema








class UsesRemaining(BaseSchema):
    # Cart swagger.json

    
    total = fields.Int(required=False)
    
    app = fields.Int(required=False)
    
    user = fields.Int(required=False)
    

